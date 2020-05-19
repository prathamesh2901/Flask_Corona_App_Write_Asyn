from flask_restful import Resource, reqparse
from models.country import CountryModel
from datetime import date


class Country(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('cases', type = int, required = True, help = 'This is a required field')
    parser.add_argument('deaths', type = int, required = True, help = 'This is a required field')
    parser.add_argument('recoveries', type = int, required = False,)

    def put(self, name):

        data = Country.parser.parse_args()
        today = str(date.today())
        country = CountryModel(name, today, **data)

        country.send_to_queue()

        return country.json()
