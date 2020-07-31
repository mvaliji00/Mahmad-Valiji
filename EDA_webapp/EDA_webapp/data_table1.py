import pandas as pd
import pickle

def get_table1Data(filepath,username):
    ### -----> Load Data
    try:
        df = pickle.load(open('data/' + username + '/' + filepath, 'rb'))
    except (OSError, IOError) as e:
        df = pickle.load(open('data/' + filepath, 'rb'))

    if df.columns.values[0] == 'Unnamed: 0':
        df = df.drop('Unnamed: 0', axis=1)

    df_head = df.head()
    df_describe = df.describe()

    missing_count = (df.isna().sum() / df.shape[0]) * 100
    valid_count = 100 - missing_count
    df_quality = pd.DataFrame([valid_count,missing_count],index=['valid', 'missing'])

    unique_values = df.nunique()
    col = df_head.columns.values
    val = unique_values

    temp = [str(i) + ' Unique Values' if i > 50 else str(i) + ' Categories' for i in val]
    category = pd.DataFrame([temp], columns=col, index=['Uniqueness'])

    data = pd.concat([category, df_describe, df_head,df_quality], sort=False)
    data = data.reset_index().rename(columns={'index': 'Index'})

    data.index = data.index.values
    json = data.to_json(orient='records')
    return json

#k,v = get_table1Data('csv_salesforceData.pkl')