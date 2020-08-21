import pandas as pd
import pickle as pkl
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pkl.load(open('quality_people.pkl','rb'))

df_base = df['Base Data']
df_edu = df['Education']
df_pm = df['Professional Membership']
df_wexp = df['Previous Work Experience']
df_learn = df['Learning History']

## Assessment of Education ##
df_edu = df_edu.drop(['University/College/Institution','Year Awarded'],axis=1)
# for col in df_edu:
#     print(df_edu[col].unique())

#check user with education history
df_edu_filled = df_edu[df_edu['Subject/Major'] != 'No Further Education'] #29 people
degree_type_count