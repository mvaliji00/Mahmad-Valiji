import pandas as pd
import pickle

def source_data():
    # df = pd.DataFrame([['a', 'b'], ['c', 'd']],
    #                 index=['col 1', 'col 2'],
    #                 columns=['col 1', 'col 2'])
    # json = df.to_json(orient='records')

    ### -----> Load Data
    df = pickle.load(open('../SalesForce EDA/pickleFiles/raw_salesforceData.pkl', 'rb'))
    df_head = df.head()
    df_describe = df.describe()

    missing_count = (df.isna().sum() / df.shape[0]) * 100
    valid_count = 100 - missing_count
    df_quality = pd.DataFrame([valid_count,missing_count],index=['valid', 'missing'])

    unique_values = df.nunique()
    col = df_head.columns.values
    val = unique_values

    temp = [str(i) + ' Unique Values' if i > 50 else str(i) + ' Categories' for i in val]
    category = pd.DataFrame([temp], columns=col, index=[''])

    data = pd.concat([category, df_describe, df_head,df_quality])#, sort=True)
    data = data.reset_index().rename(columns={'index': 'Index'})

    data.index = data.index.values  # ['a', 'b', 'c','d','e','f','g','h','j','k','l','i','v','p']
    json = data.to_json(orient='records')

    return json

#k,v = source_data()
#print(v)