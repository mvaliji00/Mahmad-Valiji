import pandas as pd
import numpy as np
import re
import string
from sklearn.feature_extraction.text import CountVectorizer
#pd.set_option('display.max_columns', 1000)

## Read data from excel
readData = pd.read_excel('../NLE.xlsx',sheet_name="Summary Breakdown")
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
data_clean = pd.DataFrame(data_df.transcript.apply(round1))
print(data_clean)

## Round2: Clean the data

data_clean.to_pickle('data_clean.pkl')

cv = CountVectorizer(stop_words='english')
data_cv = cv.fit_transform(data_clean.transcript)
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_dtm.index = data_clean.index

