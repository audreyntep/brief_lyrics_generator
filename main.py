from flask import Flask
from flask_restful import Resource, Api, reqparse
from models import get_lstm_generator

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return 'ML LYRICS GENERATOR'

class LSTM_model(Resource):
    def get(self, lyrics):
        lyrics_generated = get_lstm_generator(lyrics)
        return {'lstm_generated_text' : lyrics_generated}

class Transformer_model(Resource):
    def get(self, lyrics):
        lyrics_generated = get_lstm_generator(lyrics)
        return {'transformer_generated_text': lyrics_generated}

api.add_resource(Home, '/')
api.add_resource(LSTM_model, '/lstm/<string:lyrics>')
api.add_resource(Transformer_model, '/transformer/<string:lyrics>')


if __name__ == '__main__':
    app.run(debug=True)