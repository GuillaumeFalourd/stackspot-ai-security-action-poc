# Vulnerability 9: Using Components with Known Vulnerabilities
import requests

def fetch_data(url):
    response = requests.get(url)
    return response.text

# Vulnerability 10: Insufficient Logging & Monitoring
def process_data(data):
    try:
        # Process data
        pass
    except Exception as e:
        # Insufficient logging
        print("An error occurred")

# Example usage
print(fetch_data("http://example.com"))
process_data("some data")