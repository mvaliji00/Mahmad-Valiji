import os
import json

def get_dataSources(user):
    check  = os.path.isdir('data/'+ user)
    if check:
        user_files = os.listdir('data/' + user)
    else:
        os.mkdir('data/' + user)
        folder = os.listdir('data/' + user)
        user_files = [f for f in folder if os.path.isfile(os.path.join('data/',f))]

    general_files = [f for f in os.listdir('data/') if os.path.isfile(os.path.join('data/',f))]
    files = general_files + user_files
    json_string = json.dumps(files)
    return json_string