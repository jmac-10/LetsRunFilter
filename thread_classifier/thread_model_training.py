import pandas as pd
import nltk
from preprocessing import preprocess
from imblearn.over_sampling import SMOTE
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
import joblib

nltk.download('stopwords')
nltk.download('wordnet')

threads = pd.read_csv("less_threads.csv", header=None, names=["Title", "Author", "RR?"])

# combine thread title and author as X variable, classification as Y
x = threads["Title"] + " " + threads["Author"]
y = threads["RR?"]

# Preprocess text
x = preprocess(x)
# convert text to tfidf values
vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
x = vectorizer.fit_transform(x).toarray()
# oversample nrr
oversample = SMOTE()
x, y = oversample.fit_resample(x, y)

# split train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# train classifiers
rf_classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
rf_classifier.fit(x_train, y_train)
lr_classifier = LogisticRegression()
lr_classifier.fit(x_train, y_train)

# test and evaluate
print("random forest")
rf_y_pred = rf_classifier.predict(x_test)
print(confusion_matrix(y_test, rf_y_pred))
print(classification_report(y_test, rf_y_pred))
print(accuracy_score(y_test, rf_y_pred))
print()
print("logit")
lr_y_pred = lr_classifier.predict(x_test)
print(confusion_matrix(y_test, lr_y_pred))
print(classification_report(y_test, lr_y_pred))
print(accuracy_score(y_test, lr_y_pred))

with open('ThreadClassifier.pkl', 'wb') as f:
    joblib.dump(rf_classifier, f)

with open('ThreadClassifierVocab.pkl', 'wb') as f2:
    joblib.dump(vectorizer.vocabulary_, f2)
