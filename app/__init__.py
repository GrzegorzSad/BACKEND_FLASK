from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.route("/")
    def hello_world():
        return "<a>test init</a>"
    
    return app