import plotly
import plotly.graph_objs as go
import numpy as np
import json


def dataTable():
    #trace = go.Figure(data=[go.table(header=dict(values=['A Scores', 'B Scores']),
    #             cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
    #                 ])

    count = 500
    xScale = np.linspace(0, 100, count)
    yScale = np.random.randn(count)

    # Create a trace
    trace = go.Scatter(
        x=xScale,
        y=yScale
    )

    data = [trace]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON