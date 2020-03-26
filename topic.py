import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 1000)
import pickle

with open('model2.pkl', 'rb') as f:
    data = pickle.load(f)

df = pd.DataFrame(data)
df.columns = ['Words', 'Topics', 'Percentages']

table = pd.pivot_table(df,index=['Topics'],columns=['Words'], aggfunc=np.sum, fill_value=0)
table.columns = table.columns.droplevel(0)
del table.columns.name

table.index = table.index.astype(int)
table.sort_index(inplace=True)
table = table.astype(float)

topics = pd.DataFrame()
topics = pd.DataFrame(columns=['Output'])

for i in range(20):
    topic = table.sort_values(by=i, axis=1, ascending=False)
    topic = topic.iloc[i, :20].index.values
    topic = ", ".join(topic)

    temp = pd.DataFrame([topic], columns=['Output'], index=['Topic ' + str(i+1)])
    topics = topics.append(temp)

print(topics)
topics.to_csv (r'topics_dataframe.csv', index = True, header=True)