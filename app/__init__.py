# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler
from os import path
from pymongo import MongoClient
from flask_cors import CORS
from flask_threaded_sockets import Sockets, ThreadedWebsocketServer
from app.home import ws


mongo_client = MongoClient()
mongo_client = MongoClient('mongodb://172.16.0.11:27017/')

db = SQLAlchemy()
login_manager = LoginManager()

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)

def register_blueprints(app):
    for module_name in ('base', 'home'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)




def websocketThread(app):
    sockets = Sockets(app)
    sockets.register_blueprint(ws, url_prefix=r'/')



def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def create_app(config):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    CORS(app)
    websocketThread(app)
    return app
