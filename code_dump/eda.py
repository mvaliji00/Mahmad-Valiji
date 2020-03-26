from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture as GMM
import numpy as np
import pandas as pd
from nltk import word_tokenize
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

pd.set_option('display.max_rows', 1000)

# dataset = pd.read_pickle("data_clean.pkl")
# dataset = word_tokenize(dataset.loc['NLE','transcript'])
# print(dataset)

with open('data_clean.pkl', 'rb') as f:
    dataset = pickle.load(f)

#dataset = np.load('data_clean.npy')
print(dataset)


# # train model
#model = Word2Vec([dataset], window=5, min_count=1, sg=1)
# # summarize vocabulary
# words = list(model.wv.vocab)
#
# # fit a 2d PCA model to the vectors
# X = model[model.wv.vocab]
# pca = PCA(n_components=2)
# result = pca.fit_transform(X)
#
# # GMM clustering
# gmm = GMM(n_components=20, covariance_type='full').fit(result)
#
# labels = gmm.predict(result)
# prob = gmm.predict_proba(result).round(3)
# topic_prob = np.amax(prob, axis=1)[:, np.newaxis]
#
# words = np.transpose(words)[:, np.newaxis]
# topics = np.transpose(labels)[:, np.newaxis]
# AR = np.hstack((words, topics, topic_prob))
#
# np.save("model.npy",AR)
# #np.save("model2.npy",AR)
#
# sns.scatterplot(x=result[:, 0], y=result[:, 1], hue=labels, palette="Paired")
# print(labels)
# plt.show()