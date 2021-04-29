# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager,mongo_client
from jinja2 import TemplateNotFound
from app.home.mongo_cmd import MongoClient
from werkzeug.routing import BaseConverter




def admin(args):
    pass


@blueprint.route('/index')
@login_required
def index():
    try:
        return render_template('index.html', segment='index',db=MongoClient.list_databases(),conn_users=MongoClient.connection_users('admin'))
    except Exception as err:
        print(err)
        return render_template('page-500.html', segment='index')

@blueprint.route('/<db_name>')
@login_required
def db_info(db_name):
    try:
        return render_template('collections.html', segment='dbname',collections=MongoClient.collection_get(db_name))
    except Exception as err:
        print(err)
        return render_template('page-500.html', segment='index')

@blueprint.route('/<db_name>/<collection>')
@login_required
def collection_info(db_name,collection):
    try:
        return render_template('documents.html', segment='collections',documents=MongoClient.documents_get(db_name,collection))
    except Exception as err:
        print(err)
        return render_template('page-500.html', segment='index')



def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
