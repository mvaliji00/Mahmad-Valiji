from bokeh.plotting import figure
from bokeh.embed import file_html
from flask import Markup
from bokeh.resources import CDN

def dataPlot():
    plot = figure()
    xdata = range(1, 6)
    ydata = [x*x for x in xdata]
    plot.line(xdata, ydata)
    return Markup(file_html(plot,CDN))