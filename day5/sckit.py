from sklearn.model_selection import train_test_split
import seaborn as sns
import pandas as pd
import numpy as np
iris = sns.load_dataset('iris')

x = iris.iloc[:,0:4]
y = iris.iloc[:, 4]
# x= iris[['sepal_length','sepal_width','petal_length','petal_width']]
# y = iris['species']

# print(x)
# print(y)

x_train , x_test, y_train, y_test = train_test_split(x,y,test_size= 0.2)
# training qns, exam qns, training ans, exam ans
print(x_train.shape)
print(y_train.shape)