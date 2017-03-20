# Imports
from bson import ObjectId
from flask import Flask, request, json, jsonify, Response, render_template
from pymongo import MongoClient
import getpass
import socket
import datetime
import time

# Creator of BootOwl

__creator__ = 'Erick Fernando Cobo Enriquez'

# Instance Initialization
app = Flask(__name__)

# Database Connection
try:
    uri = "mongodb://ecoboe249:viper1829@ds153609.mlab.com:53609/bootowl"
    client = MongoClient(uri)
    data_base = client.get_default_database()
    collection = data_base.get_collection("boot_owl_activity_log")
    data_base_test = client.test
except Exception as e:
    print('Exception Raised: Couldn\'t connect to server!!!!' + str(e))

# Obtains username from current user.
user_id = getpass.getuser()

# Creates a timestamp
time = time.time()
time_stamp = datetime.datetime.utcnow()


# We use this method to handle 404 errors, in case the user enters a wrong input.
@app.errorhandler(500)
def internal_server_failure():
    return render_template('500.html'), 500


@app.errorhandler(405)
def wrong_method():
    return render_template('405.html'), 405


@app.errorhandler(404)
def not_found():
    return render_template('404.html'), 404


@app.errorhandler(400)
def wrong_request():
    return render_template('400.html'), 400


def database_failure(exception):
    return str(exception) + 'Could not connect to Data Base'


# This method allows BootOwl to store a new ability, which he will be able to execute in another method.
@app.route('/api/learn/', methods=['POST'])
def learn():
    in_args = request.args
    action_code = in_args['action_code']
    name = in_args['name']

    try:
        collection.insert_one(
            {
                'user': user_id,
                'name': name,
                'api_code': action_code,
                'date': time_stamp
            }
        )
    except Exception as exception:
        return database_failure(exception)

    result = {
        'user': user_id,
        'name': name,
        'api_code': action_code,
        'date': time_stamp
    }

    return Response(json.dumps(result), status=200, mimetype='application/json')


# This method allows BootOwl to forget an ability. This is a DELETE in the data base.
@app.route('/api/forget/<name>', methods=['POST', 'GET'])
def forget(name):
    try:
        collection.delete_one(
            {
                "user": user_id,
                "name": name
            }
        )

    except Exception as exception:
        database_failure(exception)

    results = {'user': user_id,
               'name': name}
    return Response(json.dumps(results), status=200, mimetype='application/json')


# This method allows BootOwl to update an abilities name. This is an UPDATE in the data base.
@app.route('/api/update/<doc_id>/', methods=['POST'])
def update(doc_id):
    in_args = request.args
    new_name = in_args['new_name']
    result = ''
    try:
        collection.update_one(
            {'_id': ObjectId(doc_id)},
            {'$set': {
                'name': new_name
            }
            }, upsert=False,
            bypass_document_validation=True)

        result = {
            'name': new_name
        }

    except Exception as exception:
        database_failure(exception)

    return Response(json.dumps(result), status=200, mimetype='application/json')


# This let's BootOwl to print his current abilities.
@app.route('/api/log/', methods=['GET'])
def print_log():
    result = []
    try:
        trick_list = data_base.get_collection("boot_owl_activity_log")

        for query in trick_list.find():
            result.append(
                {'user': query['user'],
                 'name': query['name'],
                 'api_code': query['api_code'],
                 'date': query['date']
                 })

    except Exception as exception:
        database_failure(exception)

    return Response(json.dumps(result), status=200, mimetype='application/json')


# This method prints Boot Owl's current possible states.
@app.route('/api/state/', methods=['GET'])
def print_state():
    result = []
    try:
        state_lists = data_base.get_collection("boot_owl_activity_log")
        for query in state_lists.find():
            result.append({'api_code': query['api_code'], 'name': query['name']})
    except Exception as exception:
        database_failure(exception)

    return Response(json.dumps(result), status=200, mimetype='application/json')


# This allows Boot Owl to execute code commands, couldn't manage to execute functions.
@app.route('/api/execute-action/<doc_id>/', methods=['POST'])
def execute_code(doc_id):
    action = None

    try:
        for query in collection.find({'_id': ObjectId(doc_id)}):
            action = query['api_code']
    except Exception as exception:
        database_failure(exception)

    exec(action)

    return Response(json.dumps(action), status=200)


@app.route('/api/add/', methods=['GET', 'POST'])
def add():
    in_args = request.args
    param1 = in_args['num1']
    param2 = in_args['num2']
    add_result = []
    try:
        add_result = int(param1) + int(param2)
    except Exception as exception:
        database_failure(exception)

    result = {
        'result': {
            'add_result': add_result
        },
        'param1': param1,
        'param2': param2
    }

    return Response(json.dumps(result), status=200, mimetype='application/json')


@app.route('/api/subtract/', methods=['GET', 'POST'])
def subtract():
    in_args = request.args
    param1 = in_args['num1']
    param2 = in_args['num2']
    add_result = []
    try:
        add_result = int(param1) - int(param2)
    except Exception as exception:
        database_failure(exception)

    result = {
        'result': {
            'add_result': add_result
        },
        'param1': param1,
        'param2': param2
    }

    return Response(json.dumps(result), status=200, mimetype='application/json')


@app.route('/api/multiply/', methods=['GET', 'POST'])
def multiply():
    in_args = request.args
    param1 = in_args['num1']
    param2 = in_args['num2']
    add_result = []
    try:
        add_result = int(param1) * int(param2)
    except Exception as exception:
        database_failure(exception)

    result = {
        'result': {
            'add_result': add_result
        },
        'param1': param1,
        'param2': param2
    }

    return Response(json.dumps(result), status=200, mimetype='application/json')


@app.route('/api/divide/', methods=['GET', 'POST'])
def divide():
    in_args = request.args
    param1 = in_args['num1']
    param2 = in_args['num2']
    add_result = []
    try:
        add_result = int(param1) / int(param2)
    except Exception as exception:
        database_failure(exception)

    result = {
        'result': {
            'add_result': add_result
        },
        'param1': param1,
        'param2': param2
    }

    return Response(json.dumps(result), status=200, mimetype='application/json')


# Displays a nice heart-warming greeting to a user. This is the main page.
@app.route('/', methods=['GET'])
def index():
    return Response(render_template('index.html'), status=200)


# Gets ip address for local host testing.
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

# Starts the application.
if __name__ == '__main__':
    app.run(debug=True, port=5000, host=ip)
