import requests
import time
import json
import os

# Step 1: Authentication to obtain access token
def get_access_token(account_slug, client_id, client_secret):
    url = f"https://idm.stackspot.com/{account_slug}/oidc/oauth/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'client_id': client_id,
        'grant_type': 'client_credentials',
        'client_secret': client_secret
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

CHANGED_FILES = os.getenv("CHANGED_FILES")
print("Changed files:", CHANGED_FILES)

for file_path in CHANGED_FILES:
    print(f'File Path: {file_path}')
    # Open the file and read its content
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Replace the placeholders with your actual data
    CLIENT_ID =  os.getenv("CLIENT_ID")
    CLIENT_KEY = os.getenv("CLIENT_CLIENT_KEYSECRET")
    ACCOUNT_SLUG = 'stackspot'
    QC_SLUG = 'sast-rqc'
    YOUR_DATA = file_content

    # Execute the steps
    access_token = get_access_token(ACCOUNT_SLUG, CLIENT_ID, CLIENT_KEY)
    execution_id = create_rqc_execution(QC_SLUG, access_token, YOUR_DATA)
    execution_status = get_execution_status(execution_id, access_token)

    # Extract the 'answer' field from the step_result (note: removing the leading and trailing ```json and ``` for correct JSON parsing)
    answer_str = execution_status['steps'][0]['step_result']['answer'][7:-3].replace('\\n', '\n').replace('\\"', '"')
    answer_data = json.loads(answer_str)
    vulnerabilities_amount = len(answer_data)

    print(f"\n{vulnerabilities_amount} item(s) have been found for file {file_path}:")

    # Iterate through each item and print the required fields
    for item in answer_data:
        print(f"\nTitle: {item['title']}")
        print(f"Severity: {item['severity']}")
        print(f"Correction: {item['correction']}")
