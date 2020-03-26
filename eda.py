from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture as GMM
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

with open('data_clean.pkl', 'rb') as f:
    dataset = pickle.load(f)

# train model
model = Word2Vec([dataset], window=8, min_count=1, sg=1)
# summarize vocabulary
words = list(model.wv.vocab)

# fit a 2d PCA model to the vectors
X = model[model.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)

# GMM clustering
gmm = GMM(n_components=20, covariance_type='full').fit(result)

labels = gmm.predict(result)
prob = gmm.predict_proba(result).round(3)
topic_prob = np.amax(prob, axis=1)[:, np.newaxis]

words = np.transpose(words)[:, np.newaxis]
topics = np.transpose(labels)[:, np.newaxis]
AR = np.hstack((words, topics, topic_prob))

## Save data
with open('model.pkl', 'wb') as f:
   pickle.dump(AR, f)

## Plot model
sns.scatterplot(x=result[:, 0], y=result[:, 1], hue=labels, palette="muted")
plt.title('TEXT TYPE 1: Win Size = 8')
plt.legend(loc='lower right')
plt.show()