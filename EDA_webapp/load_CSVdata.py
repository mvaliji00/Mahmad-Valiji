import pickle
import pandas as pd

def save_CSVdata():
    filepath = '../SalesForce EDA/pickleFiles/df_extract.csv'
    df = pd.read_csv(filepath)

    ## save CSV data
    pickle.dump(df, open('data/csv_salesforceData.pkl', 'wb'))
    print('CSV data is loaded..')