from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config') 
    db.init_app(app)
    migrate.init_app(app, db)

    from server.routes import api_bp
    app.register_blueprint(api_bp)

    return app
