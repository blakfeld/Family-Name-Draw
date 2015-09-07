"""
app.py -- Main entry point for this application.
"""

import os
import json

import bottle
from bottle import get, put, run, template, static_file, response, request

from db import FamilySQLiteDB


MY_PATH = os.path.dirname(os.path.abspath(__file__))


"""
Frontend Serving Routes ***********************************
"""


@get('/')
def index():
    for member in db.get_all_members():
        print member.name

    print db.get_member_by_id(2).name

    return template('index')


"""
API Routes ************************************************
"""


@get('/api/members')
def get_members():
    members = db.get_all_members()

    data = {
        'members': [m.__dict__ for m in members]
    }

    response.content_type = 'application/json'

    return json.dumps(data)


@get('/api/members/<id>')
def get_specific_member(id):
    member = db.get_member_by_id(int(id))

    data = {
        'members': [member.__dict__]
    }

    response.content_type = 'application/json'

    return json.dumps(data)


@put('/api/members/<id>')
def put_specific_member(id):
    body = request.json

    print body
    db.update_chosen(id, body['chosenUserId'])

    response.status = 201

    return json.dumps({})


@get('/api/availablemembers/<current_user>')
def get_available_members(current_user):
    members = db.get_available_members(current_user)

    for m in members:
        print m.name
    data = {
        'members': [m.__dict__ for m in members]
    }

    response.content_type = 'application/json'

    return json.dumps(data)


"""
Static File Routes ****************************************
"""


@get('/<filename:re:.*\.js>')
def javascripts(filename):
    js_path = os.path.join(MY_PATH, 'static', 'js')
    return static_file(filename, root=js_path)


@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    css_path = os.path.join(MY_PATH, 'static', 'css')
    return static_file(filename, root=css_path)


@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    img_path = os.path.join(MY_PATH, 'static', 'img')
    return static_file(filename, root=img_path)


@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    font_path = os.path.join(MY_PATH, 'static', 'fonts')
    return static_file(filename, root=font_path)


if __name__ == '__main__':
    bottle.TEMPLATE_PATH.append(os.path.join(MY_PATH, 'views'))

    db = FamilySQLiteDB(os.path.join(MY_PATH, '..', 'family_gift_app.db'))

    run(host='0.0.0.0', port=9001)
