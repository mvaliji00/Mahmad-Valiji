from werkzeug.utils import secure_filename
import pickle
import pandas as pd

def save_file(uploaded_file,username):
    df = pd.read_csv(uploaded_file)
    pickle.dump(df, open('data/' + username + '/' + secure_filename(uploaded_file.filename[:-4]) + '.pkl', 'wb'))
    return 'file uploaded successfully'