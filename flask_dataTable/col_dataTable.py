import pandas as pd
import pickle

def dataColTable():
    ### -----> Load Data
    df = pickle.load(open('data/extract_salesforceData.pkl', 'rb'))
    unique_values = df.nunique()
    column_names = df.columns.values
    missing_count = (df.isna().sum() / df.shape[0])*100
    valid_count = 100 - missing_count

    col_names = ['name','valid','missing','unique','value']

    list = pd.DataFrame(columns = col_names)

    for i in range(2):
        k = df.iloc[:, i].value_counts(normalize=True) * 100
        k1 = k.index.values.tolist()
        k1 = [str(i) for i in k1]
        # table_1 = pd.DataFrame({
        #     column_names[i]: [valid_count[i], missing_count[i], unique_values[i], k1[0]]
        # },
        #     index=['Valid', 'Missing', 'Unique', 'Most Common'])
        new_row = {'name': column_names[i], 'valid': valid_count[i],'missing': missing_count[i],'unique': unique_values[i],'value': k1[0]}
        list = list.append(new_row, ignore_index=True)

    list.set_index('name', inplace=True)
    json = list.to_json(orient='index')

    return json

k = dataColTable()
print(k)