# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="harisudhan",
#   password="hari4127@"
# )

# print(mydb)

import os
import pandas as pd
df = pd.read_csv(r"Data/test.csv")
mark_name = os.listdir(r'D:\AIML-MIT\Doc\12TH')
fname = [item.split('.')[0] for item in mark_name ]
name = df['Name'].isna().sum()
df.loc[df['Name'].isna(), 'Name'] = fname[:name]
data = pd.DataFrame({'name' : fname})
data.to_csv(r'D:\Git file\Data-Science\Data-Science\day4\name.csv')
print(df)