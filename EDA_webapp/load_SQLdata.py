import pandas as pd
import pyodbc as sql
import pickle

def save_SQLdata():
    ServerName = 'LORDWSQL01\DW_Live'
    DBName = 'DW_Mirrored_Data'

    # Create connection string
    conn = sql.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'Server=' + ServerName + ';'
                          'Database=' + DBName + ';'
                          'Trusted_Connection=yes;')

    SQL_Query = pd.read_sql_query('''select * FROM [DW_Mirrored_Data].[src_salesforce_uk].[Opportunity]''', conn )
    df = pd.DataFrame(SQL_Query)

    ## save SQL data
    pickle.dump(df, open('data/raw_salesforceData.pkl', 'wb'))
    print('SQL data is loaded..')
