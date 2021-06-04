import os
from flask import Flask
from dotenv import load_dotenv
from extensions import db

from api.controller.todos import todos

load_dotenv()

def register_extensions(app) :
    db.init_app(app)

def register_router(app, prefix="/api/v1") :
    app.register_blueprint(todos, url_prefix=f"{prefix}/todos")

def create_app(config_filename) :
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False

    register_extensions(app)
    register_router(app)

    return app


app = create_app(os.environ['APP_SETTINGS'])


if __name__ == "__main__" :
    app.run()
