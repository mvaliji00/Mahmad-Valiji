from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture as GMM
import numpy as np
import seaborn as sns

# define training data
text = [
    ['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
    ['this', 'is', 'the', 'second', 'sentence'],
    ['yet', 'another', 'sentence'],
    ['one', 'more', 'sentence'],
    ['and', 'the', 'final', 'sentence']
]

# train model
model = Word2Vec(text, min_count=1)
# summarize vocabulary
words = list(model.wv.vocab)

# fit a 2d PCA model to the vectors
X = model[model.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)

# create a scatter plot of the projection
#plt.scatter(result[:, 0], result[:, 1])
#for i, word in enumerate(words):
#    plt.annotate(word, xy=(result[i, 0], result[i, 1]))

# GMM clustering
gmm = GMM(n_components=3, covariance_type='full').fit(result)
labels = gmm.predict(result)
prob = gmm.predict_proba(result).round(3)
topic_prob = np.amax(prob, axis=1)[:, np.newaxis]

words = np.transpose(words)[:, np.newaxis]
topics = np.transpose(labels)[:, np.newaxis]
AR = np.hstack((words, topics, topic_prob))

#plt.scatter(result[:, 0], result[:, 1], c=labels, s=40, cmap='viridis');
#plt.show()

# print(labels)
# plt.scatter(result[:, 0], result[:, 1], c=labels, s=10)
# plt.show()

x = [1, 3, 4, 6, 7, 9]
y = [0, 0, 5, 8, 8, 8]
classes = [0,0,1,2,2,2]
colours = ['r', 'r', 'b', 'g', 'g', 'g']

sns.scatterplot(x=x, y=y, hue=classes)
plt.show()

