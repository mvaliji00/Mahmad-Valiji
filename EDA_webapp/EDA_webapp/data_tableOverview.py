import pandas as pd
import pickle
import numpy as np

def get_overviewTableData(filepath,username):
    ### -----> Load Data
    try:
        df = pickle.load(open('data/' + username + '/' + filepath, 'rb'))
    except (OSError, IOError) as e:
        df = pickle.load(open('data/' + filepath, 'rb'))

    if df.columns.values[0] == 'Unnamed: 0':
        df = df.drop('Unnamed: 0', axis=1)

    data = pd.DataFrame(columns=['Desc','Type'])

    ## General section


    ## cardinality
    cardinality = df.nunique()[df.nunique() >= 30].apply(str)
    df2 = pd.DataFrame({'Desc': cardinality.index.values + ' has a high cardinality: ' + cardinality.values + ' distinct values',
                        'Type': 'High Cardinality'
                        })
    data = data.append(df2,ignore_index=True)

    ## correlation
    correlation = df.corr()
    correlation = correlation[correlation >= 0.8] #.dropna()
    df2 = pd.DataFrame(columns=['Type','Desc'])
    for i in range(correlation.shape[0]):
        corr = correlation.iloc[i,:].dropna().drop(correlation.index.values[i])
        if not corr.empty:
            df2 = df2.append({'Desc': correlation.index.values[i] + ' is highly correlated with ' + ' & '.join(corr.index.values),
                              'Type': 'Correlation'},ignore_index=True)
    data = data.append(df2,ignore_index=True)

    ## missing
    missing = df.isna().sum()
    missing = missing[missing >= df.shape[0]*.01]
    missing_prec = ((missing/df.shape[0])*100).round(1)
    df2 = pd.DataFrame({'Desc': missing.index.values + ' has ' + missing.apply(str).values + '('+ missing_prec.apply(str).values + '%) missing values',
                       'Type':'Missing'})
    data = data.append(df2,ignore_index=True)

    ## skewness
    skew = df.skew(axis = 0, skipna = True).round(1).apply(str)
    df2 = pd.DataFrame({'Desc': skew.index.values + ' is highly skewed (γ1=' + skew.values + ')',
                        'Type':'Skewness'})
    data = data.append(df2,ignore_index=True)

    ## unique values
    unique_values = df.nunique()[df.nunique() >= df.shape[0]*.9].apply(str)
    df2 = pd.DataFrame({'Desc': unique_values.index.values + ' has unique values',
                        'Type':'Unique Values'})
    data = data.append(df2,ignore_index=True)

    ## zeros
    zeros = df.shape[0] - np.count_nonzero(df, axis=0)
    df2 = pd.DataFrame(zeros,index=df.columns.values)
    df2 = df2[df2[0] != 0]
    df_perc = ((df2[0]/df.shape[0])*100).round(1)
    df2 = pd.DataFrame({'Desc': df2.index.values + ' has ' + df2[0].apply(str).values + ' (' + df_perc.apply(str).values + '%) zeros',
                        'Type':'Zeros'})
    data = data.append(df2,ignore_index=True)

    #data.index = data.index.values
    json = data.to_json(orient='records')
    return json

#k,v = get_overviewTableData('k')
