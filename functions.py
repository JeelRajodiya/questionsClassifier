import joblib
import sklearn


vectorizer = joblib.load('svm_vectorizer.pkl')
svm = joblib.load('svm_model.pkl')
def predict(text):
    #  Run this command to publish
    # az webapp up --name QuestionsClassifier --resource-group cloud-shell-storage-centralindia --sku F1
    vectorized = vectorizer.transform([text])
    return svm.predict(vectorized)[0]
def predArray(textArray):
	vectorized = vectorizer.transform(textArray)
	return svm.predict(vectorized)


# print(predict('What is the weather today?'))
