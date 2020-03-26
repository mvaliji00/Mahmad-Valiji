import pandas as pd
import numpy as np
from nltk import word_tokenize
from nltk.corpus import stopwords

data = pd.read_pickle('data_clean.pkl')
dataset = word_tokenize(data.loc['NLE','transcript'])

stop_words = stopwords.words('english')
list = ['oh','di','mott','macdonald','harris','jon','austin','battersea','ii','co','x']
stop_words.extend(list)

data = []
for word in dataset:
    if word not in stop_words:
        data.append(word)

print(data)
# np.save("data_clean.npy",data)
#
# dataset2 = np.load('data_clean2.npy')
# dataset2 = dataset2.tolist()
#
# for sentence in dataset2:
#     for word in sentence:
#         if word in stop_words:
#             sentence.remove(word)
#
# #np.save("data_clean2.npy",dataset2)
