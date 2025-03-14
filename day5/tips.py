import seaborn as sns
tips_df = sns.load_dataset('tips')
print(tips_df.head())
tips_df['day'].unique()
import matplotlib.pyplot as plt 
x = tips_df['d']
plt.show()