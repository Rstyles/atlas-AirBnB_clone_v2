#!/usr/bin/python3
from flask import Flask, request

# Create the Flask application instance
app = Flask(__name__)

# Define routes and views
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)