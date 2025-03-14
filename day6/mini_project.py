from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.model_selection import  train_test_split
from sklearn.neighbors import KNeighborsClassifier 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv('Data/heart.csv')
target = df['target']


x = df.iloc[:,:13]
y = df['target']

x_train, x_test, y_train , y_test = train_test_split(x,y, test_size= 0.2, random_state= 42)

knn = KNeighborsClassifier(n_neighbors= 4)
knn.fit(x_train, y_train)

rf = RandomForestClassifier(random_state= 300)
rf.fit(x_train, y_train)
predict = rf.predict(x_test)
prediction = knn.predict(x_test)

# print(accuracy_score(prediction, y_test)*100)
print(accuracy_score(predict, y_test)*100)