# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# da = np.array([1,3,6,9,12,15,18,21,24,27,30,100])
# sns.boxplot(da)
# plt.show()

# Heatmap, pairplot, countplot, swarmplot and stripplot

import seaborn as sns
iris = sns.load_dataset('iris')
iris.to_csv(r'C:\Users\STUDENT\Desktop\Python\Data\iris2.csv')
print(iris)