from flask import Flask,render_template,request,redirect
from data_table1 import get_table1Data
from data_table1_chart import get_table1chartData
from data_table2 import get_table2Data
from data_tableOverview import get_overviewTableData
from listofdatafiles import get_dataSources
from load_SQLdata import save_SQLQuery_data, save_SQLDB_data
from load_CSVdata import save_CSVdata
from save_uploadedFile import save_file
import os

### script to load data into the data folder for the app
#save_SQLQuery_data() ##fetch data from SQL Server (single Query)
#save_SQLDB_data()  ##fetch data from SQL Server (full DB)
#save_CSVdata()  ##fetch data from CSV file

### launch web app on port 5000
app = Flask(__name__)
username = ''

### http routes
@app.route("/get-overviewtable-data")
def get_data5():
    filename  = request.args.get('source')
    response5 = get_overviewTableData(filename,username)
    return response5

@app.route("/get-table1-data")
def get_data():
    filename  = request.args.get('source')
    response1 = get_table1Data(filename,username)
    return response1

@app.route("/get-table1-chartdata")
def get_data3():
    filename = request.args.get('source')
    response3 = get_table1chartData(filename,username)
    return response3

@app.route("/get-table2-data")
def get_data2():
    filename = request.args.get('source')
    response2 = get_table2Data(filename,username)
    return response2

@app.route("/get-datasources")
def get_data4():
    global username
    username = os.getlogin()
    response4 = get_dataSources(username)
    return response4

### rest api to upload user files
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    #global username
    #username = os.getlogin()
    if request.method == 'POST':
        file = request.files['file']
        save_file(file,username)
        return redirect('/')

### define loading html page
@app.route('/')
def index():
    return render_template('dashboard.html')

### debug component
if __name__ == "__main__":
    app.run(debug=True)
