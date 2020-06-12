import pandas as pd
import string
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
import pickle

data = pd.read_excel('NLE.xlsx',sheet_name='Summary Breakdown')
data = data.iloc[:,1].dropna()

## function to remove punctuation
def clean_text_round1(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    return text

## Utilise remove punctuation function and clean the data
round1 = lambda x: clean_text_round1(x)
data_clean = data.apply(round1)
data_clean = [word_tokenize(sentence) for sentence in data_clean]

# Round2: Clean the data
stop_words = stopwords.words('english')
list = ['oh','di','mott','macdonald','harris','jon','austin','battersea','ii','co','x']
stop_words.extend(list)

for sentence in data_clean:
    for word in stop_words:
        if word in sentence:
            sentence.remove(word)

with open('data_clean2.pkl', 'wb') as f:
    pickle.dump(data_clean, f)
