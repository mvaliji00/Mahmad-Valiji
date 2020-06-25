from flask import Flask,render_template,jsonify
from dataTable import source_data
from col_dataTable import dataColTable

app = Flask(__name__)

@app.route("/get-data")
def get_data():
    response1 = source_data()
    return response1

@app.route("/get-data2")
def get_data2():
    response2 = dataColTable()
    return response2

@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
