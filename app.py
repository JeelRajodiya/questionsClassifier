from flask import Flask, request
import logging
from functions import predict
#  Run this command to publish
# az webapp up --name QuestionsClassifier --resource-group cloud-shell-storage-centralindia --sku F1
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run()
