from flask import Flask,render_template,jsonify
from data_table1 import table1_data
from data_table2 import table2_data
from chart_table2 import table1_chart_data

app = Flask(__name__)

@app.route("/get-data")
def get_data():
    response1 = table1_data()
    return response1

@app.route("/get-data2")
def get_data2():
    response2 = table2_data()
    return response2

@app.route("/get-data3")
def get_data3():
    response3 = table1_chart_data()
    return response3

@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
