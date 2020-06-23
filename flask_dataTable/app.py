from flask import Flask,render_template,jsonify
from dataTable import source_data

app = Flask(__name__)

@app.route("/get-data")
def get_data():
    response = source_data()
    return response
    #return jsonify({"a": 1, "b": 2})

@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
