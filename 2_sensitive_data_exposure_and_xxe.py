# Vulnerability 3: Sensitive Data Exposure
import json

def save_user_data(user_data):
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)

# Vulnerability 4: XML External Entities (XXE)
import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    return root

# Example usage
user_data = {"username": "admin", "password": "password123"}
save_user_data(user_data)

xml_data = """<?xml version="1.0"?>
<!DOCTYPE root [
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>&xxe;</root>"""
print(parse_xml(xml_data))