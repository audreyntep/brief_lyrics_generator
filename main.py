from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return 'ML LYRICS GENERATOR'


class LSTM_model(Resource):
    def get(self):
        return {'model': 'LSTM'}


class Transformer_model(Resource):
    def get(self):
        return {'model': 'Transformer_model'}

api.add_resource(Home, '/')
api.add_resource(LSTM_model, '/lstm')
api.add_resource(Transformer_model, '/transformer')


if __name__ == '__main__':
    app.run(debug=True)