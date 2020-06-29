from bokeh.models import ColumnDataSource, TableColumn,DataTable,HTMLTemplateFormatter
from bokeh.embed import file_html
from flask import Markup
from bokeh.resources import CDN
import pickle
import pandas as pd
from bokeh.plotting import figure
from bokeh.layouts import column,row,gridplot,layout
from data_hbar_bokeh import dataPlot_hbar

def dataColTable():
    ### -----> Load Data
    df = pickle.load(open('/data/extract_salesforceData.pkl', 'rb'))
    unique_values = df.nunique()
    column_names = df.columns.values
    missing_count = (df.isna().sum() / df.shape[0])*100
    valid_count = 100 - missing_count

    list = []
    for i in range(10):
        k = df.iloc[:,i].value_counts(normalize=True) * 100
        k1 = k.index.values.tolist()
        k1 = [str(i) for i in k1]

        table_1  = pd.DataFrame({
                                    column_names[i]: ['', unique_values[i], '', 'Unique Values',''],
                                    'a': ['Valid', 'Missing', 'Unique', 'Most Common',''],
                                    'b': [valid_count[i], missing_count[i], unique_values[i], k1[0],'']
                                 },
                                index=['', '', '', '', ''])

        columns_1 = [TableColumn(field=column_names[i], title=column_names[i]),
                     TableColumn(field='a', title=""),
                     TableColumn(field='b', title="")]

        source_data_1 = ColumnDataSource(table_1)
        data_table_1 = DataTable(source=source_data_1, columns=columns_1, editable=False,index_position=None,height=150)
        hbar = dataPlot_hbar(610, valid_count[i], missing_count[i], 35)

        # l = layout([
        #     [data_table_1]
        # ])
        l = data_table_1
        list.append(l)
        list.append(hbar)

    col = column(list)
    return Markup(file_html(col, CDN))

def get_panda_data():
    ### -----> Load Data
    df = pickle.load(open('../SalesForce EDA/pickleFiles/extract_salesforceData.pkl', 'rb'))
    unique_values = df.nunique()
    column_names = df.columns.values
    missing_count = (df.isna().sum() / df.shape[0])*100
    valid_count = 100 - missing_count

    list = []
    for i in range(10):
        k = df.iloc[:,i].value_counts(normalize=True) * 100
        k1 = k.index.values.tolist()
        k1 = [str(i) for i in k1]

        table_1 = pd.DataFrame({'column1': column_names[i], 'column2': ''}, index=[1])
        table_2 = pd.DataFrame({'column1': [unique_values[i],'Unique Values']}, index=[1, 2])

        table_3 = pd.DataFrame({'column1': ['Valid', 'Missing', 'Unique', 'Most Common'],
                                'column2': [valid_count[i], missing_count[i], unique_values[i], k1[0]]},
                               index=[1, 2, 3, 4])

        # template = """
        #     <p style="font-size:15"
        #     </p>
        # """
        # fmt = HTMLTemplateFormatter(template=template)

        columns_1 = [TableColumn(field="column1", title="column2"),TableColumn(field="column2", title="column2")]
        columns_2 = [TableColumn(field="column1", title="column2")]

        source_data_1 = ColumnDataSource(table_1)
        data_table_1 = DataTable(source=source_data_1, columns=columns_1, editable=False, fit_columns=False,
                               index_position=None, width = 200,height = 30,header_row=False)

        source_data_2 = ColumnDataSource(table_2)
        data_table_2 = DataTable(source=source_data_2, columns=columns_2, editable=False, fit_columns=False,
                                 index_position=None,width = 200, height=150, header_row=False,sizing_mode="stretch_height")

        source_data_3 = ColumnDataSource(table_3)
        data_table_3 = DataTable(source=source_data_3, columns=columns_1, editable=False, fit_columns=False,
                                 index_position=None, sizing_mode="stretch_width", height=150, header_row=False)

        hbar = dataPlot_hbar(610, valid_count[i], missing_count[i],35)

        i  = layout([
            [data_table_1,hbar],[data_table_2,data_table_3]
        ])
        list.append(i)

    return Markup(file_html(list, CDN))

def template_data():
    # tags = ["<h1>Example header</h1>",
    #         '<div style="color: red;">Example div</div>',
    #         '<input type="text" name="example_form" \
    #         placeholder="Example input form">'
    #         ]
    #
    # pd.set_option('display.max_colwidth', -1)

   # tags_frame = pd.DataFrame(tags, columns=["Tag Example"])
    hbar = dataPlot_hbar(610, 60, 40, 35)
    mark = Markup(file_html(hbar, CDN))

    tags_frame = pd.DataFrame({'Column Name': [1, 2, 3, 4,mark], ' ': [1, 2, 3, 4, 5], '': [1, 2, 3, 4, 5]},
                           index=['', '', '', '', ''])

    tags_html = tags_frame.to_html(escape=False)

    return tags_html

