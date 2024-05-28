from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from backend.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__, static_folder='../frontend')
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from backend.routes.auth import auth
    from backend.routes.ocr import ocr
    app.register_blueprint(auth)
    app.register_blueprint(ocr)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    @app.route('/app.js')
    def serve_js():
        return send_from_directory(app.static_folder, 'app.js')

    @app.route('/style.css')
    def serve_css():
        return send_from_directory(app.static_folder, 'style.css')

    return app
