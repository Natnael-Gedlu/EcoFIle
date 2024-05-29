#!/usr/bin/python3
"""
Defines routes for user authentication.
"""

from flask import Blueprint, request, jsonify
from backend import db, bcrypt
from backend.models import User
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['POST'])
def register():
    """
    Registers a new user.

    Returns:
        JSON response with a message and status code.
    """
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201


@auth.route('/login', methods=['POST'])
def login():
    """
    Logs in an existing user.

    Returns:
        JSON response with a message and status code.
    """
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user, remember=data.get('remember', False))
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Login failed'}), 401


@auth.route('/logout')
@login_required
def logout():
    """
    Logs out the current user.

    Returns:
        JSON response with a message and status code.
    """
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200
