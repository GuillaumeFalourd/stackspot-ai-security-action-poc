#!/usr/bin/python3
import datetime
import requests
import ast
import csv
import time
import json
import os

def create_report():
    directory = 'vulnerability_reports'
    if not os.path.exists(directory):
        os.makedirs(directory)

    current_date = datetime.datetime.now()
    current_date_format = current_date.strftime("%m-%d-%Y-%Hh%M")
    current_date_format_string = str(current_date_format)
    file_name = "vulnerabilities-" + current_date_format_string + ".csv"
    file_path = os.path.join(directory, file_name)
    return file_path

def json_to_csv(file_path, json_data, csv_file_path):
    # Open the CSV file in append mode
    with open(csv_file_path, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write the header if the file is empty
        if csv_file.tell() == 0:
            header = ["file", "title", "severity", "correction", "lines"]
            writer.writerow(header)
        
        # Write the data
        for item in json_data:
            row = [file_path, item['title'], item['severity'], item['correction'], item['lines']]
            writer.writerow(row)

def save_output(name: str, value: str):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output_file:
        print(f'{name}={value}', file=output_file)

# Step 1: Authentication to obtain access token
def get_access_token(account_slug, client_id, client_key):
    url = f"https://idm.stackspot.com/{account_slug}/oidc/oauth/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'client_id': client_id,
        'grant_type': 'client_credentials',
        'client_secret': client_key
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    return response_data['access_token']

# Step 2: Creation of a Quick Command (RQC) execution
def create_rqc_execution(qc_slug, access_token, input_data):
    url = f"https://genai-code-buddy-api.stackspot.com/v1/quick-commands/create-execution/{qc_slug}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    data = {
        'input_data': input_data
    }

    # print('File data to analyze:', data) 
    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        decoded_content = response.content.decode('utf-8')  # Decode bytes to string
        extracted_value = decoded_content.strip('"')  # Strip the surrounding quotes
        response_data = extracted_value
        print('ExecutionID:', response_data)
        return response_data
    else:
        print(response.status_code)
        print(response.content)

# Step 3: Polling for the execution status
def get_execution_status(execution_id, access_token):
    url = f"https://genai-code-buddy-api.stackspot.com/v1/quick-commands/callback/{execution_id}"
    headers = {'Authorization': f'Bearer {access_token}'}
    i = 0
    while True:
        response = requests.get(
            url, 
            headers=headers
        )
        response_data = response.json()
        status = response_data['progress']['status']
        if status in ['COMPLETED', 'FAILED']:
            return response_data
        else:
            print("Status:", f'{status} ({i})')
            print("Execution in progress, waiting...")
            i+=1
            time.sleep(5)  # Wait for 5 seconds before polling again

# Replace the placeholders with your actual data
CLIENT_ID =  os.getenv("CLIENT_ID")
CLIENT_KEY = os.getenv("CLIENT_KEY")
ACCOUNT_SLUG = os.getenv("CLIENT_REALM")
QC_SLUG = os.getenv("QC_SLUG")
CHANGED_FILES = os.getenv("CHANGED_FILES")

print(f'\033[36mFiles to analyze: {CHANGED_FILES}\033[0m')
CHANGED_FILES = ast.literal_eval(CHANGED_FILES)
all_result = []
report_path = create_report()
try:
    for file_path in CHANGED_FILES:
        print(f'\n\033[36mFile Path: {file_path}\033[0m')
        # Open the file and read its content
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Execute the steps
        access_token = get_access_token(ACCOUNT_SLUG, CLIENT_ID, CLIENT_KEY)
        execution_id = create_rqc_execution(QC_SLUG, access_token, file_content)
        execution_status = get_execution_status(execution_id, access_token)

        result = execution_status['result']

        # Remove the leading and trailing ```json and ``` for correct JSON parsing
        if result.startswith("```json"):
            result = result[7:-4].strip()

        result_data = json.loads(result)

        vulnerabilities_amount = len(result_data)

        print(f"\n\033[36m{vulnerabilities_amount} item(s) have been found for file {file_path}:\033[0m")

        # Iterate through each item and print the required fields
        for item in result_data:
            print(f"\nTitle: {item['title']}")
            print(f"Severity: {item['severity']}")
            print(f"Correction: {item['correction']}")
            print(f"Lines: {item['lines']}")

        if len(result_data) > 0:
            save_output('result', result_data)
            json_to_csv(file_path, result_data, report_path)
            
except OSError as e:
    print(f"An error occurred while creating the directory or file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
