import os
import json

def get_dataSources():
    arr = os.listdir('data/')
    json_string = json.dumps(arr)
    return json_string