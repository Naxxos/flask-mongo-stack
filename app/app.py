import os
from flask import request, jsonify

from pymongo import MongoClient
from flask import Flask


application = Flask(__name__)

#application.config["MONGO_URI"] = "mongodb://admin:password1@mongo:27017/mongodb"

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + \
    os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + \
    ':27017/' + os.environ['MONGODB_DATABASE']

mongo = MongoClient(host='mongo',
                         port=27017,
                         username=os.environ['MONGODB_USERNAME'],
                         password=os.environ['MONGODB_PASSWORD'],
                         authSource="admin")
db = mongo["mongodb"]


@application.route('/')
def index():
    return jsonify(
        status=True,
        message="Other two",
    )


@application.route('/todo')
def todo():
    _todos = db.todo.find()

    item = {}
    data = []
    for todo in _todos:
        item = {
            'id': str(todo['_id']),
            'todo': todo['todo']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )


@application.route('/todo', methods=['POST'])
def createTodo():
    data = request.get_json(force=True)
    item = {
        'todo': data['todo']
    }
    db.todo.insert_one(item)

    return jsonify(
        status=True,
        message='To-do saved successfully!'
    ), 201


if __name__ == "__main__":

    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(port=ENVIRONMENT_PORT,
                    debug=ENVIRONMENT_DEBUG)
