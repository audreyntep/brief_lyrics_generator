from flask import Flask
from flask_restful import Resource, Api, reqparse

from models import run_lstm_predict as lstm



app = Flask(__name__)
api = Api(app)

MODEL ='LSTM_simple_model_v3.h5'
VOCAB = 'vocab_v3.txt'

class Home(Resource):
    def get(self):
        return 'ML LYRICS GENERATOR'

class LSTM_model(Resource):
    def get(self, seed):
        quantity = 100
        #seed = 'you are the sunshine of my life that s why i ll always be around you are the apple of'
        lyrics_generated = lstm.LSTM_prediction(MODEL, VOCAB, quantity).generate_text(seed)
        return {'lstm_generated_text' : lyrics_generated}


class Transformer_model(Resource):
    def get(self, seed):
        lyrics_generated = seed
        return {'transformer_generated_text': lyrics_generated}

api.add_resource(Home, '/')
api.add_resource(LSTM_model, '/lstm/<string:seed>')
api.add_resource(Transformer_model, '/transformer/<string:seed>')


if __name__ == '__main__':
    app.run(debug=True)