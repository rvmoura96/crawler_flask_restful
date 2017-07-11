from flask   import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import requests
import re

app = Flask(__name__)
api = Api(app)

class Search(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('url', type=str, help='Site informado')
            parser.add_argument('word', type=str, help='Palavra a ser pesquisada')
            args = parser.parse_args()
            url = args['url']
            word = args['word']
            page = requests.get(url).text
            count = len(re.findall(word, page))

            _searchCount= count

            data = {'Ocorrencias': count}
           
            return jsonify(data)

        except Exception as e:
            return {'error': str(e)}

api.add_resource(Search, '/search')

if __name__ == '__main__':
    app.run(debug=True)