"""
Initializes the Flask application and its components.
"""

from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from backend.config import Config
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        Flask app instance.
    """
    app = Flask(__name__, static_folder='../frontend')
    app.config.from_object(Config)

    # Set the upload folder configuration
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    from backend.routes.auth import auth
    from backend.routes.ocr import ocr
    app.register_blueprint(auth)
    app.register_blueprint(ocr)

    with app.app_context():
        from backend.models import User
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        """
        Loads a user by ID.
        Args:
            user_id (int): The ID of the user to load.
        Returns:
            User: The loaded user object.
        """
        return User.query.get(int(user_id))

    @app.route('/')
    def index():
        """
        Serves the index HTML file.
        Returns:
            Response: The index HTML file.
        """
        return app.send_static_file('index.html')

    @app.route('/app.js')
    def serve_js():
        """
        Serves the app.js file.
        Returns:
            Response: The app.js file.
        """
        return send_from_directory(app.static_folder, 'app.js')

    @app.route('/style.css')
    def serve_css():
        """
        Serves the style.css file.
        Returns:
            Response: The style.css file.
        """
        return send_from_directory(app.static_folder, 'style.css')

    return app
