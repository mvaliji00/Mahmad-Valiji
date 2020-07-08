from flask import Flask,render_template,jsonify
from dataTable import source_data
from col_dataTable import dataColTable
from chart_table2 import table1_chart_data
from test import list_of_source_data
from run_before import run

# script to load data into the data folder for the app
run()

# launch web app on port 5000
app = Flask(__name__)

@app.route("/get-data")
def get_data():
    response1 = source_data()
    return response1

@app.route("/get-data2")
def get_data2():
    response2 = dataColTable()
    return response2

@app.route("/get-data3")
def get_data3():
    response3 = table1_chart_data()
    return response3

@app.route("/get-data4")
def get_data4():
    response4 = list_of_source_data()
    return response4

@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
