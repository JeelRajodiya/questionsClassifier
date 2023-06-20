import joblib
import sklearn


def predict(text):
    #  Run this command to publish
    # az webapp up --name QuestionsClassifier --resource-group cloud-shell-storage-centralindia --sku F1
    svm = joblib.load('svm_model.pkl')
    vectorizer = joblib.load('svm_vectorizer.pkl')
    vectorized = vectorizer.transform([text])
    return svm.predict(vectorized)[0]


# print(predict('What is the weather today?'))
