from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.cli import bp as cli_bp
    app.register_blueprint(cli_bp)

    @app.route("/")
    def hello_world():
        return "<a>test init</a>"
    
    return app

from app import models