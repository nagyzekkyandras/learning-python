from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

COUNTRIES = {
    '1' : {'name': 'Austria', 'capital': 'Vienna' },
    '2' : {'name': 'Bulgaria', 'capital': 'Sofia' },
    '3' : {'name': 'Canada', 'capital': 'Ottawa' }
}

parser = reqparse.RequestParser()


class ContriesList(Resource):
    def get(self):
        return COUNTRIES

    def post(self):
        parser.add_argument("name")
        parser.add_argument("capital")
        args = parser.parse_args()
        country_id = int(max(COUNTRIES.keys())) + 1
        country_id = '%i' % country_id
        COUNTRIES[country_id] = {
            "name": args["name"],
            "capital": args["capital"]
        }
        return COUNTRIES[country_id], 201

class Country(Resource):
    def get(self, country_id):
        if country_id not in COUNTRIES:
            return "Not found", 404
        else:
            return COUNTRIES[country_id]

    def put(self, country_id):
        parser.add_argument("name")
        parser.add_argument("capital")
        args = parser.parse_args()
        if country_id not in COUNTRIES:
            return "Record not found", 404
        else:
            country = COUNTRIES[country_id]
            country["name"] = args["name"] if args["name"] is not None else country["name"]
            country["capital"] = args["capital"] if args["capital"] is not None else country["capital"]
            return country, 200

    def delete(self, country_id):
        if country_id not in COUNTRIES:
            return "Not found", 404
        else:
            del COUNTRIES[country_id]
            return '', 204

api.add_resource(ContriesList, '/countries')
api.add_resource(Country, '/<country_id>')

if __name__ == '__main__':
    app.run(debug=True, port=5000)