import pickle
import pandas as pd

def save_CSVdata():
    filepath = '../SalesForce EDA/pickleFiles/df_extract.csv'
    df = pd.read_csv(filepath)
    saved_filename = 'sql_salesforceData'

    ## save CSV data
    pickle.dump(df, open('data/' + saved_filename +'.pkl', 'wb'))
    print('CSV data is loaded..')