import pandas as pd
import pickle
import numpy as np

def dataColTable():
    ### -----> Load Data
    df = pickle.load(open('../SalesForce EDA/pickleFiles/raw_salesforceData.pkl', 'rb'))
    unique_values = df.nunique()
    column_names = df.columns.values
    missing_count = df.isna().sum()     # / df.shape[0]) * 100
    valid_count = df.shape[0] - missing_count

    unique_perc = np.round((df.nunique()/df.shape[0])*100,2)
    missing_perc = np.round((missing_count/ df.shape[0]) * 100,2)
    valid_perc = np.round(100 - missing_perc,2)
    #missing_count = (df.isna().sum() / df.shape[0]) * 100
    #valid_count = 100 - missing_count

    col_names = ['name', 'valid', 'missing', 'unique', 'value','valid_perc','missing_perc', 'unique_perc','value_perc']

    list = pd.DataFrame(columns=col_names)
    #column_names.size
    for i in range(column_names.size):
        k = df.iloc[:, i].value_counts(normalize=True) * 100
        #print(k)
        k1 = k.index.values.tolist()
        if k1:
            k2 = np.round(k.values.tolist()[0],2)
            k1 = [str(i) for i in k1]
            new_row = {'name': column_names[i], 'valid': valid_count[i], 'missing': missing_count[i],
                       'unique': unique_values[i], 'value': k1[0], 'valid_perc': valid_perc[i],
                       'missing_perc': missing_perc[i], 'unique_perc': unique_perc[i], 'value_perc': k2}
            list = list.append(new_row, ignore_index=True)
        else:
            k2 = ""
            new_row = {'name': column_names[i], 'valid': valid_count[i], 'missing': missing_count[i],
                       'unique': unique_values[i], 'value': "", 'valid_perc': valid_perc[i],
                       'missing_perc': missing_perc[i], 'unique_perc': unique_perc[i], 'value_perc': k2}
            list = list.append(new_row, ignore_index=True)


    list.set_index('name', inplace=True)
    json = list.to_json(orient='index')
    return json

#k, v= dataColTable()
#print(k)

def dataColTable2():
    ### -----> Load Data
    df = pickle.load(open('../SalesForce EDA/pickleFiles/extract_salesforceData.pkl', 'rb'))
    unique_values = df.nunique()
    column_names = df.columns.values
    missing_count = (df.isna().sum() / df.shape[0])*100
    valid_count = df.shape[0] - missing_count

    col_names = ['name','valid','missing','unique','value']
    list = pd.DataFrame(columns = col_names)
    #list = []
    name = []
    #print(column_names.size)
    for i in range(2):
        k = df.iloc[:, i].value_counts(normalize=True) * 100
        k1 = k.index.values.tolist()
        k1 = [str(i) for i in k1]
        table_1 = pd.DataFrame({
            'a': ['Valid', 'Missing', 'Unique', 'Most Common'],
            'b': [valid_count[i], missing_count[i], unique_values[i], k1[0]]
        },
            index=[column_names[i], column_names[i], column_names[i], column_names[i]])

        test =  {
            column_names[i]: ['Valid', 'Missing', 'Unique', 'Most Common'],
            column_names[i]: [valid_count[i], missing_count[i], unique_values[i], k1[0]]
        }
        new_row = {'name': column_names[i], 'valid': valid_count[i],'missing': missing_count[i],'unique': unique_values[i],'value': k1[0]}

        k = pd.DataFrame({
            'a': ['Valid', 'Missing', 'Unique', 'Most Common'],
            'b': [valid_count[i], missing_count[i], unique_values[i], k1[0]]
        },
        index=[column_names[i], column_names[i],column_names[i],column_names[i]])
        #name.append(column_names[i])
        ##list.append(new_row)

        list = list.append(new_row, ignore_index=True)
    #data = pd.concat(list)#,keys=name)#.reset_index(drop=True)
    #list.set_index('name', inplace=True)
    json = list.to_json(orient='index')
    print(json)
    return json
