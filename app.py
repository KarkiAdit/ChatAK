from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response
import nltk
nltk.download('punkt')

app = Flask(__name__)
CORS(app)


@app.route("/")
def show():
    return render_template("index.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
