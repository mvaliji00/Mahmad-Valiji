import pandas as pd
import pickle
from bokeh.models import ColumnDataSource, TableColumn,DataTable
from bokeh.embed import file_html
from flask import Markup
from bokeh.resources import CDN
from bokeh.layouts import column,row,gridplot,layout
from data_hbar_bokeh import dataPlot_hbar
from data_vbar_bokeh import dataPlot_vbar

def dataTable():
    ### -----> Load Data
    df = pickle.load(open('../SalesForce EDA/pickleFiles/extract_salesforceData.pkl', 'rb'))
    df_head = df.head()
    df_describe = df.describe()

    unique_values = df.nunique()
    col = df_head.columns.values
    val = unique_values

    temp = [str(i) + ' Unique Values' if i > 50 else str(i) + ' Categories' for i in val]
    category = pd.DataFrame([temp], columns=col, index=[''])

    data = pd.concat([category, df_describe, df_head], sort=True)
    data = data.reset_index().rename(columns={'index': 'Index'})

    ### -----> Automate extraction of df columns
    data_columns = data.columns.values
    columns = []
    hbar_list = []
    vbar_list = []

    for i in data_columns:
        wdth = (len(i) * 8)+50
        temp = TableColumn(field=i, title=i, width=wdth)
        columns.append(temp)

        ## missing data plot
        if  i!= 'Index':
            null_count = df[i].isna().sum() / df.shape[0]
            fill_count = 1 - null_count
        else:
            null_count = 0
            fill_count = 0

        plt1 = dataPlot_hbar(wdth,fill_count,null_count)
        hbar_list.append(plt1)

        ## bar chart plot
        if  i!= 'Index':
            k = df[i].value_counts(normalize=True) * 100
            k1 = k.index.values.tolist()
            k1 = [str(i) for i in k1]
            k2 = k.values.tolist()
            # k1 = ['False', 'True']
            # k2 = [86.85380116959064, 13.146198830409356]
        else:
            k1 = ['']
            k2 = [0]

        plt2 = dataPlot_vbar(wdth,k1[:10],k2[:10])
        vbar_list.append(plt2)



    return Markup(file_html(l, CDN))
