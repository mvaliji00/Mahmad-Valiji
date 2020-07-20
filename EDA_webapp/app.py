from flask import Flask,render_template,request,redirect
from data_table1 import get_table1Data
from data_table1_chart import get_table1chartData
from data_table2 import get_table2Data
from listofdatafiles import get_dataSources
from load_SQLdata import save_SQLQuery_data, save_SQLDB_data
from load_CSVdata import save_CSVdata
from save_uploadedFile import save_file

### script to load data into the data folder for the app
#save_SQLQuery_data() ##fetch data from SQL Server (single Query)
#save_SQLDB_data()  ##fetch data from SQL Server (full DB)
#save_CSVdata()  ##fetch data from CSV file

### launch web app on port 5000
app = Flask(__name__)

### http routes
@app.route("/get-table1-data")
def get_data():
    filename  = request.args.get('source')
    response1 = get_table1Data(filename)
    return response1

@app.route("/get-table1-chartdata")
def get_data3():
    filepath = request.args.get('source')
    response3 = get_table1chartData(filepath)
    return response3

@app.route("/get-table2-data")
def get_data2():
    filepath = request.args.get('source')
    response2 = get_table2Data(filepath)
    return response2

@app.route("/get-datasources")
def get_data4():
    response4 = get_dataSources()
    return response4

### rest api to upload user files
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      file = request.files['file']
      save_file(file)
      return redirect('/')

### define loading html page
@app.route('/')
def index():
    return render_template('dashboard.html')

### debug component
if __name__ == "__main__":
    app.run(debug=True)
