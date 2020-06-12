import pandas as pd
import numpy as np
import re
import string
from nltk import word_tokenize
from nltk.corpus import stopwords
import pickle

#pd.set_option('display.max_columns', 1000)
## Read data from excel
readData = pd.read_excel('NLE.xlsx',sheet_name="Summary Breakdown")
readData = readData.iloc[:,1].dropna()

## Project list definition
project_list = ["NLE"]

## function to combine seperate string elements
def combine_text(list_of_text):
    combined_text = ' '.join(list_of_text)
    return combined_text

## Operation to utilise above function and combine the data
data_combined = {}
for proj in project_list:
    data_combined[proj] = [combine_text(readData)]

## Convert the dict to pandas df
data_df = pd.DataFrame.from_dict(data_combined).transpose()
data_df.columns = ['transcript']

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
dataset = pd.DataFrame(data_df.transcript.apply(round1))

# Round2: Clean the data
dataset = word_tokenize(dataset.loc['NLE','transcript'])
stop_words = stopwords.words('english')
list = ['oh','di','mott','macdonald','harris','jon','austin','battersea','ii','co','x']
stop_words.extend(list)

data_clean = []
for word in dataset:
    if word not in stop_words:
        data_clean.append(word)

with open('data_clean.pkl', 'wb') as f:
    pickle.dump(data_clean, f)
