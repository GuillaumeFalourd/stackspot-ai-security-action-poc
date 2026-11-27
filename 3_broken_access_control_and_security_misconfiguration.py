# Vulnerability 5: Broken Access Control
def get_admin_data(user_role):
    if user_role == "admin":
        return "Sensitive admin data"
    else:
        return "Access denied"

# Vulnerability 6: Security Misconfiguration
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the home page!"

# Example usage
print(get_admin_data("user"))

if __name__ == "__main__":
    app.run(debug=True)  # Debug mode should not be used in production