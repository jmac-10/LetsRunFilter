from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer



def preprocess(x):
    """Preprocesses the combined thread and author and converts
    to tfidf features"""

    # change shoe brands to 'shoebrand'
    x.replace('(?i)asics|nike|adidas|hoka|brooks|puma|new balance|oiselle|saucony', 'shoebrand', regex=True,
              inplace=True)
    # change interval descriptions to 'intervals'
    x.replace('(?i)[0-9]+x([0-9]{2,4}|[a-z]+)', 'intervals', regex=True, inplace=True)
    # change times to 'time'
    x.replace('[0-9]{0,2}((:[0-9]{2})|(\\.[0-9]+))', 'time', regex=True, inplace=True)
    # change common race distances to 'distance'
    x.replace('(?i)[0-9]+(m|yd|km|mi|k)', 'distance', regex=True, inplace=True)
    # remove special characters
    x.replace('\\W', ' ', regex=True, inplace=True)
    # remove single characters
    x.replace('\\s+[a-zA-Z]\\s+', ' ', regex=True, inplace=True)
    # remove single character from start
    x.replace('\\^[a-zA-Z]\\s+', ' ', regex=True, inplace=True)
    # remove multiple spaces
    x.replace('\\s+', ' ', regex=True, inplace=True)
    # to lowercase
    x = x.str.lower()
    # lemmatize
    stemmer = WordNetLemmatizer()
    x.apply(lambda text: [stemmer.lemmatize(word) for word in text.split()])

    return x
