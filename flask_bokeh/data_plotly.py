import plotly
#import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import json

def line():
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