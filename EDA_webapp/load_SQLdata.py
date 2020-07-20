import pandas as pd
import pyodbc as sql
import pickle

def save_SQLQuery_data():
    ServerName = 'LORDWSQL01\DW_Live'
    DBName = 'DW_Mirrored_Data'
    saved_filename = 'csv_salesforceData'

    # Create connection string
    conn = sql.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'Server=' + ServerName + ';'
                          'Database=' + DBName + ';'
                          'Trusted_Connection=yes;')


    SQL_Query = pd.read_sql_query('''select * FROM [DW_Mirrored_Data].[src_salesforce_uk].[Opportunity]''', conn )
    df = pd.DataFrame(SQL_Query)
    ## save SQL data
    pickle.dump(df, open('data/' + saved_filename + '.pkl', 'wb'))
    print('SQL data is loaded..')

def save_SQLDB_data():
    ServerName = "NSWSQL16DEV\\NSWSBOX01"
    DBName = 'TemporaryWork'

    # Create connection string
    conn = sql.connect('Driver={ODBC Driver 17 for SQL Server};'
                       'Server=' + ServerName + ';'
                       'Database=' + DBName + ';'
                       'Trusted_Connection=yes;')

    SQL_DBQuery = pd.read_sql_query('''select
        s.name AS SchemaName
        ,case when o.type = 'U' THEN 'Table' ELSE 'View' END AS ObjectType
        ,o.name AS ObjectName
    from
        sys.objects o
    LEFT JOIN
        sys.schemas s
        ON o.schema_id = s.schema_id
    WHERE
        o.type = 'U'
        OR o.type = 'V' ''', conn)
    df_filenames = pd.DataFrame(SQL_DBQuery)
    df_filenames = df_filenames['ObjectName']

    for i in df_filenames:
        df = pd.read_sql_query('''select * FROM ''' + i, conn)
        pickle.dump(df, open('data/' + i + '.pkl', 'wb'))

    print('SQL data is loaded..')