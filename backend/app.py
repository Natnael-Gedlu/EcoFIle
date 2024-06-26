#!/usr/bin/python3
"""
This script initializes and runs a Flask web application.
"""
from backend import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
