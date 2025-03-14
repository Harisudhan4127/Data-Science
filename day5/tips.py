import seaborn as sns
tips_df = sns.load_dataset('tips')
print(tips_df.head())
tips_df['day'].unique()
import matplotlib.pyplot as plt 
sns.regplot (x= tips_df['total_bill'], y = tips_df['tip'], color="red")
plt.show()