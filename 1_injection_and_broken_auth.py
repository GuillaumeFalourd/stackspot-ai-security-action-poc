# Vulnerability 1: SQL Injection
import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

# Vulnerability 2: Broken Authentication
users = {"admin": "password123"}

def login(username, password):
    if username in users and users[username] == password:
        return "Login successful!"
    else:
        return "Login failed!"

# Example usage
print(get_user_data("admin' OR '1'='1"))
print(login("admin", "password123"))