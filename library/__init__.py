from flask import Flask, request, Blueprint
from library.ap.controller import applicant
from extension import db, ma
from model import Applicant, results
import os


def create_db(app):
    if not os.path.exists("appli/appli.db"):
        db.create_all(app=app)
        print("Tao DB!")


def create_app(config_file="config.py"):
    app = Flask(__name__)
    db.init_app(app)
    ma.init_app(app)
    app.config.from_pyfile(config_file)
    create_db(app)
    app.register_blueprint(applicant)
    #app.register_blueprint(borrow)
    return app
