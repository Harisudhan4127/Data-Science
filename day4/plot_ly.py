import plotly.express as px
import pandas as pd
df = pd.read_csv(r'C:\Users\STUDENT\Desktop\Python\Data\salary.csv') 
print("successfully started")
print("--------------------------------------------------")
print(df)
print("--------------------------------------------------")
print('IsNull :')
print(df.isnull(),"\n" ,df.isnull().sum())
print("--------------------------------------------------")
df["salary"] = df["salary"].fillna(df["salary"].mean())
print(df["salary"].describe())
print("--------------------------------------------------")
dept = df.groupby("dept").count()
print(dept)
print("--------------------------------------------------")
under_salary = df[df["salary"] < 20000]
print(f"Under 20k salary : \n{under_salary.to_string(index=False)}")
print("--------------------------------------------------")
df["bonus"] = df["salary"]*0.05
print(df)
df.to_csv(r"c:\Users\STUDENT\Desktop\output\salary.csv")
print("successfully finished")

