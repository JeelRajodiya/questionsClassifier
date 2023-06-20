from flask import Flask, request, jsonify
import logging
from functions import predict, predArray
#  Run this command to publish
# az webapp up --name QuestionsClassifier --resource-group cloud-shell-storage-centralindia --sku F1
app = Flask(__name__)
# app.debug = True

logging.basicConfig(level=logging.ERROR)


@app.route('/')
def hello():
    filef = open("requirements.txt", "r")

    return filef.read()


@app.route('/predict')
def predictText():
    text = request.args.get('text')
    prediction = predict(text)
    return prediction


@app.route('/predict', methods=['POST'])
def predictTextPost():
    textArray = request.get_json()

    prediction = predArray(textArray)
    return jsonify(prediction.tolist())


if __name__ == '__main__':
    app.run()
