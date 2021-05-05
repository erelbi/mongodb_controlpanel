# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint,ws
import json
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager,mongo_client
from jinja2 import TemplateNotFound
from app.home.mongo_cmd import MongoClient
from werkzeug.routing import BaseConverter
from app.base.forms import MongoDBCreateUSer
from flask import jsonify, make_response
from flask_threaded_sockets import Sockets, ThreadedWebsocketServer





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
        return render_template('page-500.html', segment='error')

@blueprint.route('/<db_name>/<collection>',methods=['GET','POST'])
@login_required
def collection_info(db_name,collection):
    if request.method == 'POST':
        status =  MongoClient.delete_document(db_name,collection,request.form['del'])
        return make_response(jsonify(status), 200)
    elif request.method == 'GET':
        try:
            return render_template('documents.html', segment='collections',documents=MongoClient.documents_get(db_name,collection),db=db_name)
        except Exception as err:
            print(err)
            return render_template('page-500.html', segment='error')

@blueprint.route('/users')
@login_required
def mongo_users():
    try:
        return render_template('users.html',segment='users',db=MongoClient.list_databases())
    except Exception as err:
        print(err)
        return render_template('page-500.html', segment='error')

@blueprint.route('/warning')
@login_required
def mongo_Logwarning():
    try:
        return render_template('startwarning.html',segment='warning')
    except Exception as err:
        print(err)
        return render_template('page-500.html', segment='error')

@blueprint.route('/getLog')
@login_required
def mongo_getLog():
    try:
        return render_template('getLog.html',segment='warning')
    except Exception as err:
        print(err)
        return render_template('page-500.html', segment='error')

@blueprint.route('/users/<db_name>',methods=['GET','POST'])
@login_required
def db_users_edit(db_name):
    try:
        createuser_form = MongoDBCreateUSer(request.form)
        print(request.form)
        if 'createuser' in request.form:
             MongoClient.mongo_create_user(db_name=db_name,user=request.form['username'],passwd=request.form['password'],role=request.form['roles'])

        return  render_template('dbusers.html',segment='db_users', db_users=MongoClient.mongo_get_users(db_name),form=createuser_form)
    except Exception as err:
        print(err)
        return  render_template('page-500.html',segment='error')


@blueprint.route('/status',methods=['GET'])
#@login_required
def monitor_admin(db_name='admin'):
    status = MongoClient.mongo_stat(db_name)

    return make_response(jsonify(status), 200)




@ws.route('/echo')
def echo_socket(socket,db_name='admin'):
    try:
        while not socket.closed:
            message = socket.receive()
            print(message)
            if message == 'warning':
                log = MongoClient.mongo_log(db_name,type='startupWarnings')
                socket.send(json.dumps(log))
            elif message == 'global':

                log = MongoClient.mongo_log(db_name, type='global')
                socket.send(json.dumps(log))
    except Exception as err:
        socket.send(json.dumps({'error':err}))
    finally:
        socket.closed

def get_segment( request ):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
