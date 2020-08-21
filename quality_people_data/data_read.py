import pickle
import pandas as pd

xls = pd.ExcelFile('Data QP Anonymised.xlsx')
print(xls.sheet_names)

df = dict()

for i in xls.sheet_names:
    df[i] = pd.read_excel('Data QP Anonymised.xlsx',sheet_name=i)

print(df['Education'].head())

pickle.dump(df,open('quality_people.pkl','wb'))