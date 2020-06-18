import dash
import dash_html_components as html

from flask import Flask, render_template

server = Flask(__name__)

@server.route('/name')
def name():
    return render_template('index.html')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

with open('templates/index.html', 'r') as f:
    layout = f.read()
    print(layout)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server, index_string=layout)

app.layout = html.Div(children='dash app'
# [
#     dcc.Graph(
#         id='example-graph',
#         figure={
#             'data': [
#                 {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#             ],
#             'layout': {
#                 'title': 'Dash Data Visualization'
#             }
#         }
#     )
# ]
)

if __name__ == '__main__':
    app.run_server(debug=True)