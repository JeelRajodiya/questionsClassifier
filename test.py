from functions import predict
import json
import html

filef = open("questions.json", "r")
data = json.load(filef)['results']
filef.close()

totalQuestions = len(data)
correct = 0
for i in range(totalQuestions):
    question = html.unescape(data[i]['question'])
    difficulty = data[i]['difficulty']
    prediction = predict(question)
    if prediction == difficulty:
        correct += 1
    else:
        print(question)
        print(difficulty)
        print(prediction)
        print()
print(correct / totalQuestions)