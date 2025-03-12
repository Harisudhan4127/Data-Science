# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv(r"Data/salary.csv")
# salary = df['salary'].fillna(df['salary'].mean())
# dept = df['dept']
# plt.xlabel("Dept")
# plt.ylabel("Salary")
# plt.bar(dept, salary)
# plt.show()
# print(salary)

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r'Data/sales.csv')
plt.title('Sales-Data')
plt.plot(df['year'], df['sales'])
plt.xlabel('year')
plt.ylabel('sales')
plt.show()
