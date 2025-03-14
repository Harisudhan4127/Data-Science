import seaborn as sns
import matplotlib.pyplot as plt
from mini_project import *

print(df.head())
corr = df.corr()
sns.heatmap(corr)

print(df.describe())

# to find age difference in target
sns.boxplot(df['age'])

test = df.groupby('sex').agg({'target' : 'count'})
print(test)

# Total count of target
print(df['target'].value_counts())

cp_gp = df.groupby('cp').agg({'target' : 'count'})
print(cp_gp)
print(df['cp'].value_counts())

# correlation bt sex and target
sns.barplot(x = df['sex'], y = df['target'])
# Correlation cp and target
sns.barplot(x = df['cp'], y = df['target'])

sns.pairplot(df, hue = 'sex')
sns.countplot(df['target'])

# outlet checking
 
# chol leveling checking
sns.swarmplot(df['chol'])

# Surgar level checking
print(df['fbs'].unique())
print(df['fbs'].value_counts())

# ECG checking
print(df['restecg'].unique())
print(df['restecg'].value_counts())
sns.swarmplot(df['restecg'])
sns.barplot(x= df['fbs'], y= df['target'])

# Trest Bps checking
sns.boxplot(df['trestbps'])
sns.boxplot(df['trestbps'])


# thalach checking
thalach = df['thalach'] > 160
print(thalach.value_counts())

# exang checking 
exang = df['exang']
print(exang.unique())

# oldpeak 
oldpeak = df['oldpeak']
sns.boxplot(oldpeak)

# slope
slope = df['slope']
print(slope.unique())
sns.barplot(x = slope, y = target)
plt.show()

print(x)
print(y)

print(df.shape)
print(df.isna().sum())
print(df['target'].unique())
