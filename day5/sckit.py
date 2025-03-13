from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
import seaborn as sns
import matplotlib.pyplot as plt
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

print(x_train.head())

knn = KNeighborsClassifier()
knn.fit(x_train,y_train)
print(knn.fit(x_train,y_train))
predictions = knn.predict(x_test)
print(predictions)