from flask_restful import Resource, reqparse
from models.state import StateModel
from datetime import date


class State(Resource):


    parser = reqparse.RequestParser()
    parser.add_argument('cases', type = int, required = True, help = 'This is a required field')
    parser.add_argument('deaths', type = int, required = True, help = 'This is a required field')
    parser.add_argument('recoveries', type = int, required = False,)


    def put(self, name, country):

        data = State.parser.parse_args()
        today = str(date.today())
        state = StateModel(name, today, **data)

        state.send_to_queue()

        return state.json()
