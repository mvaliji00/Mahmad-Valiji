import plotly
import plotly.graph_objs as go
import numpy as np
import json
import pandas as pd


def dataTable():

    data = [
        go.Table(header=dict(values=['A Scores', 'B Scores'],fill_color='paleturquoise',align='left'),
             cells=dict(values=[list(range(1,100)), list(range(1,100))],fill_color='lavender',align='left'))
        ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
