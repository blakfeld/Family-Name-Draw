"""
server.py:
    Run the family name draw server.

Usage:
    server.py [options]

Options:
    --host=HOST     Set listen address [default: 0.0.0.0]
    --port=PORT     Port number to listen on [default: 9001]
    --production    If toggled, use the Paste server, else WSGIRef.
"""
from __future__ import absolute_import, print_function

import os
import random
import sys

import bottle
from docopt import docopt

from family_members import FamilyMembers


MY_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(MY_PATH, 'static')
ASSET_PATH = os.path.join(STATIC_PATH, 'assets')
DATA_PATH = os.path.join(MY_PATH, '..', 'data.json')

app = bottle.Bottle()
family_members = FamilyMembers(DATA_PATH)


##
# Frontend Routes
##


@app.get('/')
def get_index():
    return bottle.static_file('index.html', root=STATIC_PATH)


##
# API Routes
##


@app.get('/api/v1/member')
def get_memeber_list():
    return family_members.get_all()


@app.get('/api/v1/member/<name>')
def get_specific_member(name):
    return family_members.get_by_name(name)


@app.post('/api/v1/member/<name>')
def draw_name_for_member(name):
    member_data = family_members.get_all()['data']
    user = family_members.get_by_name(name)['data'][0]
    if user['has_chosen']:
        return family_members.get_by_name(user['chosen'])

    valid_members = filter(
        lambda x: x['name'] not in user['cannot_choose'] and x['name'] != user['name'] and not x['chosen_by'],
        member_data
    )
    if len(valid_members) == 0:
        return {'data': []}
    elif len(valid_members) == 1:
        choice = valid_members[0]
    else:
        choice = valid_members[random.randrange(0, len(valid_members) - 1)]

    user['has_chosen'] = True
    user['chosen'] = choice['name']
    choice['chosen_by'] = user['name']

    new_data = map(
        lambda x: user if x['name'] == user['name'] else x,
        member_data
    )
    new_data = map(
        lambda x: choice if x['name'] == choice['name'] else x,
        new_data
    )

    result = {'data': new_data}
    family_members.update(result)

    return {'data': [choice]}


@app.post('/api/v1/control/reload')
def reload_data():
    family_members.reload()


##
# Static Routes
##


@app.get('/assets/<filename:path>')
def get_static_asset(filename):
    return bottle.static_file(filename, root=ASSET_PATH)


def serve(host, port, server):
    app.run(host=host, port=int(port), server=server)


def main():
    args = docopt(__doc__)

    host = args['--host']
    port = int(os.environ.get('PORT') or args['--port'])
    server = 'paste' if args.get('--production') else 'wsgiref'

    serve(host, port, server)


if __name__ == '__main__':
    sys.exit(main())
