# app/__init__.py

from flask import Flask
from config import Config
from .extensions import db, login_manager, migrate
from . import models
from app.models import User
from app.extensions import db
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Simple test route
    @app.route("/")
    def home():
        return "Resume Analyzer App Running 🚀"
    
    @app.route("/create-user")
    def create_user():
        user = User(username="testuser", email="test@example.com", password="123456")
        db.session.add(user)
        db.session.commit()
        return "User created!"

    return app