import pandas as pd
import pickle

def table1_chart_data():
    ### -----> Load Data
    df = pickle.load(open('data/extract_salesforceData.pkl', 'rb'))
    # df_head = df.head()
    # df_describe = df.describe()

    # unique_values = df.nunique()
    # col = df_head.columns.values
    # val = unique_values

    # temp = [str(i) + ' Unique Values' if i > 50 else str(i) + ' Categories' for i in val]
    # category = pd.DataFrame([temp], columns=col, index=[''])
    #
    # data = pd.concat([category, df_describe, df_head], sort=True)
    # data = data.reset_index()#.rename(columns={'index': 'Index'})

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
