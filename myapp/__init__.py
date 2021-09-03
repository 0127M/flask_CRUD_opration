from flask import Flask, config
from flask_sqlalchemy import SQLAlchemy
from config import app_config


db=SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    # import a module/component using its blue print handler variable
    from myapp.student_details.views import mod as student_module

    # register blue print as variable(s)
    app.register_blueprint(student_module)
    return app