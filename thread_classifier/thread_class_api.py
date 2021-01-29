import nltk
from flask import Flask
from flask import request
import joblib
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

from preprocessing import preprocess
import json
import pandas as pd

nltk.download('stopwords')
nltk.download('wordnet')

with open("ThreadClassifier.pkl", "rb") as f:
    thread_classifier = joblib.load(f)

with open("ThreadClassifierVocab.pkl", "rb") as f2:
    vocab = joblib.load(f2)


app = Flask(__name__)


@app.route('/running_related', methods=['POST'])
def predict_species():
    data = json.loads(request.data)
    combined = [x + ' ' + y for x, y in zip(data['titles'], data['authors'])]
    x = preprocess(pd.Series(combined))
    vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'), vocabulary=vocab)
    x = vectorizer.fit_transform(x).toarray()
    result = thread_classifier.predict(x)
    print([x for x in combined if result[combined.index(x)]])
    return json.dumps(result.tolist())


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run()
