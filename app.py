#!/usr/bin/env python3


from flask import Flask
from flask_restful import Api
from resources.country import Country
from resources.state import State


app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

api.add_resource(Country, '/country/<string:name>')
api.add_resource(State, '/state/<string:country>/<string:name>')

if __name__ == '__main__':
    app.run(port=5002, debug=True)
