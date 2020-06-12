from flask import Flask,render_template
#from ss.data_table import dataTable
from data_plotly import line
from data_table import dataTable

## Define variables for Exploratory Data Analysisd

#plot = dataPlot()
plot = line()
table = dataTable()

## Initiate App
app = Flask(__name__)

##
@app.route('/')
def index():
    return render_template('dashboard.html',dataTable=table,dataPlot=plot)

if __name__ == "__main__":
    app.run(debug=True)