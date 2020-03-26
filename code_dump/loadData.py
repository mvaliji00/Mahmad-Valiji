import pandas as pd
import string
from nltk import sent_tokenize,word_tokenize

data = pd.read_excel('NLE.xlsx',sheet_name='Summary Breakdown')
data = data.iloc[:,1].dropna()

def tokenizeSentences(fullCorpus):
    sent_tokenized = fullCorpus.apply(sent_tokenize)
    f = lambda sent: ''.join(ch for w in sent for ch in w if ch not in string.punctuation)
    sent_tokenized = sent_tokenized.apply(lambda row: list(map(f, row)))
    return sent_tokenized

#clean_data = tokenizeSentences(data)
#print(clean_data)

def clean_text(s):
    s = "".join([i for i in s])
    s = ''.join([i for i in s if i not in frozenset(string.punctuation)])
    return s

paragraph = [["Hello world. I am going for coffee before work!"],["Hello world. I am going for coffee before work!"]]
#data = sent_tokenize(paragraph)
#print(data)

#sentences = [word_tokenize(sentence) for sentence in data]
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in data]

sentences = [word_tokenize(sentence) for sentence in stripped]
print(sentences)

s = "string. With. Punctuation?"
exclude = set(string.punctuation)
s = ''.join(ch for ch in s if ch not in exclude)
