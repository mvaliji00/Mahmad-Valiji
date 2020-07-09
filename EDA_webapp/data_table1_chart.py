import pandas as pd
import pickle

def get_table1chartData(filepath):
    ### -----> Load Data
    df = pickle.load(open('data/'+ filepath, 'rb'))
    if df.columns.values[0] == 'Unnamed: 0':
        df = df.drop('Unnamed: 0', axis=1)

    ### -----> Automate extraction of df columns
    df_columns = df.columns.values

    df2 = pd.DataFrame(columns=df_columns)

    for i in df_columns:
        wdth = (len(i) * 8)+50

        k = df[i].value_counts(normalize=True) * 100
        k1 = k.index.values.tolist()
        k1 = [str(i) for i in k1]
        k2 = k.values.tolist()

        list = k1[:10] + k2[:10]

        if len(list) < 20:
            val = 20-len(list)
            temp = [''] * val
            list = list + temp

        df2[i] = list
        json = df2.to_json(orient='columns')
    return json

#v = table1_chart_data()
