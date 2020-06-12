from bokeh.resources import CDN
from bokeh.embed import file_html
from flask import Markup
import pandas as pd
import pickle
from bokeh.models import ColumnDataSource, TableColumn,DataTable

def dataTable():
    ### -----> Load Data
    df = pickle.load(open('../../SalesForce EDA/pickleFiles/extract_salesforceData.pkl', 'rb'))
    df_head = df.head()
    df_describe = df.describe()

    data = pd.concat([df_describe, df_head], sort=True)
    data = data.reset_index().rename(columns={'index': 'Index'})

    ### -----> Automate extraction of df columns
    data_columns = data.columns.values
    columns = []
    for i in data_columns:
        temp = TableColumn(field=i, title=i, width=len(i) * 8)
        columns.append(temp)

    source = ColumnDataSource(data)
    data_table = DataTable(source=source, columns=columns, height=400,
                           editable=False, fit_columns=False, index_position=None,sizing_mode="stretch_width")

    return Markup(file_html(data_table, CDN))
