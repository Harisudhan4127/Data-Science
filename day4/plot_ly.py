import plotly.express as px
import pandas as pd

# Read the CSV file
df = pd.read_csv(r'C:\Users\STUDENT\Desktop\Python\Data\salary.csv') 
print("successfully started")
print("--------------------------------------------------")
print(df)
print("--------------------------------------------------")
print('IsNull :')
print(df.isnull(), "\n", df.isnull().sum())
print("--------------------------------------------------")

# Fill missing salary values with the mean salary
df["salary"] = df["salary"].fillna(df["salary"].mean())
print(df["salary"].describe())
print("--------------------------------------------------")

# Group by department and count the number of employees in each department
dept = df.groupby("dept").count()
print(dept)
print("--------------------------------------------------")

# Filter employees with salary less than 20k
under_salary = df[df["salary"] < 20000]
print(f"Under 20k salary: \n{under_salary.to_string(index=False)}")
print("--------------------------------------------------")

# Calculate and add bonus column (5% of salary)
df["bonus"] = df["salary"] * 0.05
print(df)

# Save the updated DataFrame to a new CSV file
df.to_csv(r"c:\Users\STUDENT\Desktop\output\salary.csv")
print("successfully finished")

# Plotting with Plotly

# 1. Bar chart: Number of employees in each department
fig1 = px.bar(dept, x=dept.index, y='salary', labels={'salary': 'Number of Employees'},
              title="Number of Employees per Department")
fig1.show()

# 2. Scatter plot: Salary vs Bonus
fig2 = px.scatter(df, x="salary", y="bonus", color="dept", title="Salary vs Bonus",
                  labels={"salary": "Salary", "bonus": "Bonus"})
fig2.show()

# 3. Histogram: Distribution of Salaries
fig3 = px.histogram(df, x="salary", nbins=20, title="Distribution of Salaries")
fig3.show()
