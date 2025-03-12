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

# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv(r'Data/sales.csv')
# plt.title('Sales-Data')
# plt.plot(df['year'], df['sales'], )
# plt.xlabel('year')
# plt.ylabel('sales')
# plt.show()

# # dot point or scatted plot
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.random.randint(1,20, size = 10)
# y = np.random.randint(50,100, size = 10)
# plt.scatter(x,y, )
# plt.xlabel('year')
# plt.ylabel('sales')
# plt.show()

## Bar graph -> 
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv(r'Data\cinema.csv')
# plt.bar(df['movies'],df['likes'])
# plt.xlabel('Movies')
# plt.ylabel('Likes')
# plt.show()

# # histrograph to count repeat value in bar graph 
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(1,50, size = 100)
plt.hist(x , color= '#FFD700', edgecolor = '#AA6C39')
plt.show()