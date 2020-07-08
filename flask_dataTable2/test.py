import os
import json

def list_of_source_data():
    arr = os.listdir('data/')
    json_string = json.dumps(arr)
    return json_string