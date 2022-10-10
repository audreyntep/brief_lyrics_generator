# notebook model_lstm_predict_eric.ipynb

import numpy as np
import re, json
from keras.models import load_model

class LSTM_prediction():

    save = {}
    model = None
    vocabulary =  None
    word_indices = None
    indices_word = None
    sequence_length = 20
    diversity = 1
    quantity = 200

    def __init__(self, model_save, vocab_save, quantity=None):

        if quantity != None :
            self.quantity = quantity
        self.save = {'model': [model_save, vocab_save]}
        
        # load model
        self.model = load_model('models/save/'+model_save)
        #print("\nSummary of the Network: ")
        #print(model.summary())

        self.vocabulary = open('models/save/'+vocab_save, "r", encoding="utf8").readlines()
        # remove the \n at the end of the word, except for the \n word itself
        self.vocabulary = [re.sub(r'(\S+)\s+', r'\1', w) for w in self.vocabulary]
        self.vocabulary = sorted(set(self.vocabulary))

        self.word_indices = dict((c, i) for i, c in enumerate(self.vocabulary))
        self.indices_word = dict((i, c) for i, c in enumerate(self.vocabulary))


    def validate_seed(self, seed):
        # Validating that all the words in the seed are part of the vocabulary
        seed_words = seed.split(" ")
        valid = True
        for w in seed_words:
            print(w, end="")
            if w in self.vocabulary:
                print(" ✓ in vocabulary")
            else:
                print(" ✗ NOT in vocabulary")
                valid = False
        return valid


    # Functions from keras-team/keras/blob/master/examples/lstm_text_generation.py
    def sample(self, preds, temperature=1.0):
        # helper function to sample an index from a probability array
        preds = np.asarray(preds).astype('float64')
        preds = np.log(preds) / temperature
        exp_preds = np.exp(preds)
        preds = exp_preds / np.sum(exp_preds)
        probas = np.random.multinomial(1, preds, 1)
        return np.argmax(probas)


    def generate_text(self, seed):
        
        #seed = 'you are the sunshine of my life that s why i ll always be around you are the apple of'

        if self.validate_seed(seed):
            print("\nSeed is correct.\n")
            # repeat the seed in case is not long enough, and take only the last elements
            seed = " ".join((((seed+" ")*self.sequence_length)+seed).split(" ")[-self.sequence_length:])

            response = {}
            response.update(self.save)
            response['seed'] = seed
            response['diversity'] = str(self.diversity)
            response['sequence length'] = self.sequence_length
            response['quantity'] = self.quantity

            sentence = seed.split(" ")
            lyrics = []

            for i in range(self.quantity):
                x_pred = np.zeros((1, self.sequence_length, len(self.vocabulary)))
                for t, word in enumerate(sentence):
                    x_pred[0, t, self.word_indices[word]] = 1.

                preds = self.model.predict(x_pred, verbose=0)[0]
                next_index = self.sample(preds, self.diversity)
                next_word = self.indices_word[next_index]

                sentence = sentence[1:]
                sentence.append(next_word)
                #print(" "+next_word, end="")
                lyrics.append(next_word)

            response['prediction'] = ' '.join(lyrics)

            return response

        else:
            print('\033[91mERROR: Please fix the seed string\033[0m')
            exit(0)