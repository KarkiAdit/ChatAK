import imp
from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import pickle
from tensorflow.keras import layers, activations, models, preprocessing
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

pickle_in = open("word_tokenizer.pickle", "rb")
word_tokenizer = pickle.load(pickle_in)

pickle_in = open("vocab.pickle", "rb")
vocab = pickle.load(pickle_in)


def str_to_tokens(sentence: str):
    words = sentence.lower().split()
    tokens_list = list()
    b = 0
    for word in words:
        a = [x for x in vocab if x == word]
        if a == []:
            b = 1
            break
        tokens_list.append(word_tokenizer[word])
    if b == 0:
        return preprocessing.sequence.pad_sequences([tokens_list], maxlen=22, padding='post'), b
    else:
        x = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        return x, b


enc_model1 = tf.keras.models.load_model('enc_model1.h5', compile=False)
dec_model1 = tf.keras.models.load_model('dec_model1.h5', compile=False)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    seq, index = str_to_tokens(userText)
    states_values = enc_model1.predict(seq)
    empty_target_seq = np.zeros((1, 1))
    empty_target_seq[0, 0] = word_tokenizer['start']
    if index == 0:
        stop_condition = False
        decoded_translation = ''
    else:
        stop_condition = True
        decoded_translation = "sorry my maker is not bright enough to teach me such things or maybe you made a spelling mistake end"
    while not stop_condition:
        dec_outputs, h, c = dec_model1.predict(
            [empty_target_seq] + states_values)
        sampled_word_index = np.argmax(dec_outputs[0, -1, :])
        sampled_word = None
        for word, index in word_tokenizer.items():
            if sampled_word_index == index:
                decoded_translation += ' {}'.format(word)
                sampled_word = word

        if sampled_word == 'end' or len(decoded_translation.split()) > 74:
            stop_condition = True

        empty_target_seq = np.zeros((1, 1))
        empty_target_seq[0, 0] = sampled_word_index
        states_values = [h, c]

    return str(decoded_translation[:-3])


if __name__ == "__main__":
    app.run()
