# Vulnerability 7: Cross-Site Scripting (XSS)
from flask import Flask, request

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}!"

# Vulnerability 8: Insecure Deserialization
import pickle

def deserialize_data(data):
    return pickle.loads(data)

# Example usage
if __name__ == "__main__":
    app.run()

# Example of insecure deserialization
malicious_data = b"cos\nsystem\n(S'echo vulnerable'\ntR."
print(deserialize_data(malicious_data))