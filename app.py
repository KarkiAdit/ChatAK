from flask import Flask, request, jsonify

from chat import get_response

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello World! Ma Aditya ko personalized chatbot ho'


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if the text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)
