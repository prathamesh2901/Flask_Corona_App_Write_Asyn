from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.country import CountryModel


class Country(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('cases', type = int, required = True, help = 'This is a required field')
    parser.add_argument('deaths', type = int, required = True, help = 'This is a required field')
    parser.add_argument('recoveries', type = int, required = False,)

    def put(self, name):

        data = Country.parser.parse_args()
        country = CountryModel(name, **data)


        country.cases = data['cases']
        country.deaths = data['deaths']
        country.deaths = data['deaths']

        country.send_to_queue()

        return country.json()
