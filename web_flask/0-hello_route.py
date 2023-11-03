#!/usr/bin/python3
from flask import Flask, request
"""Runs a Flask web application"""
    
app = Flask(__name__)

# Define routes and views
@app.route('/')
def hello():
    return 'Hello HBNB!'

# Run the Flask application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)