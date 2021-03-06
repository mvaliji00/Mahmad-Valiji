import pandas as pd
import pickle

def table1_data():
    # df = pd.DataFrame([['a', 'b'], ['c', 'd']],
    #                 index=['col 1', 'col 2'],
    #                 columns=['col 1', 'col 2'])
    # json = df.to_json(orient='records')

    ### -----> Load Data
    df = pickle.load(open('data/extract_salesforceData.pkl', 'rb'))
    df_head = df.head()
    df_describe = df.describe()

    unique_values = df.nunique()
    col = df_head.columns.values
    val = unique_values

    temp = [str(i) + ' Unique Values' if i > 50 else str(i) + ' Categories' for i in val]
    category = pd.DataFrame([temp], columns=col, index=[''])

    data = pd.concat([category, df_describe, df_head], sort=True)
    #data = data.reset_index()#.rename(columns={'index': 'Index'}
    data.index = data.index.values      # ['a', 'b', 'c','d','e','f','g','h','j','k','l','i','v','p']
    json = data.to_json(orient='records')

    return json,data


k,v = table1_data()
print(v)