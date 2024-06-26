#!/usr/bin/python3
"""
Defines the User model for a Flask application
"""
from backend import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """
    Represents a user with id, username, email, and password.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the user.
        """
        return f'<User {self.username}>'
