import sqlite3
import pickle
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    cursor.execute(query)
    user = cursor.fetchone()

    conn.close()

    if user:
        return "Login successful!"
    else:
        return "Invalid credentials."

@app.route('/search')
def search():
    query = request.args.get('query')
    return render_template_string('<h1>Search results for: {{ query }}</h1>', query=query)

@app.route('/load')
def load():
    data = request.args.get('data')
    obj = pickle.loads(data.encode())
    return f"Loaded object: {obj}"


if __name__ == '__main__':
    app.run(debug=True)