import matplotlib.pyplot as plt
from sklearn.model_selection import  train_test_split
import seaborn as sns
import pandas as pd 

df = pd.read_csv('Data/heart.csv')
# print(df.head())
x = df.iloc[:,:13]
y = df['target']

corr = df.corr()
# sns.heatmap(corr)

# print(df.describe())

# to find age difference in target
# sns.boxplot(df['age'])

test = df.groupby('sex').agg({'target' : 'count'})
# print(test)

# Total count of target
# print(df['target'].value_counts())

# cp_gp = df.groupby('cp').agg({'target' : 'count'})
# print(cp_gp)
# print(df['cp'].value_counts())

# correlation bt sex and target
# sns.barplot(x = df['sex'], y = df['target'])
# Correlation cp and target
# sns.barplot(x = df['cp'], y = df['target'])

# sns.pairplot(df, hue = 'sex')
# sns.countplot(df['target'])

# outlet checking
 
# chol leveling checking
# max persons in chol range
# sns.swarmplot(df['chol'])

# Surgar level checking
# print(df['fbs'].unique())
# print(df['fbs'].value_counts())

# ECG checking
# print(df['restecg'].unique())
# print(df['restecg'].value_counts())
# sns.swarmplot(df['restecg'])
# sns.barplot(x= df['fbs'], y= df['target'])

# Trest Bps checking
# sns.boxplot(df['trestbps'])
# sns.boxplot(df['trestbps'])


# thalach
thalach = df['thalach'] > 160
print(thalach.value_counts())

plt.show()

# print(x)
# print(y)

# print(df.shape)
# print(df.isna().sum())
# print(df['target'].unique())

