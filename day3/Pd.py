# import pandas as pd
# # csv -> comma separated value
# df = pd.read_csv("Data\student.csv")
# # print(df["name"]) # colume to read
# # print(df[["id","name","class"]]) # Colume 
# print(df.iloc[1:4,0:2]) # Slicing function


# import pandas as pd
# data = {"id": [1,2,3,4],
#       "name": [None,"logeshwari","loki","logeshwaran"],
#       "age": [18,None,31,99],
#       "location": ["chennai","Asgard",None,"vannarupettai"],
#       "Status": ["Housewife","Director","God of story",None]}
# df = pd.DataFrame(data)
# print(df.isnull().sum())

# import pandas as pd
# data = {"id": [1,2,3,4],
#         "name": [None,"logeshwari","loki","logeshwaran"],
#         "age": [18,None,31,99],
#         "location": ["chennai","Asgard",None,"vannarupettai"],}
# df = pd.DataFrame(data)
# df["name"].fillna("Unidentified", inplace= True)
# # df["location"].dropna(inplace= True)
# print(df)

# import pandas as pd
# df = pd.read_csv("Data\Student2.csv")
# age = df["age"].mean()
# df["age"].fillna(age,inplace = True)
# df["name"].fillna('Unidentified',inplace = True)
# df["location"].fillna('-',inplace = True) 
# print(df)
# Filter method
# f_df = df[df['id']<10]
# print(f_df)
# # df.to_csv(r'C:\Users\STUDENT\Desktop\Python\Data\dummy.csv', index=False, header=True)


# Shop
# import pandas as pd
# df = pd.read_csv("Data/Student2.csv")
# total_purchased = df.groupby("purchased").agg({'cus_id' : 'count'})
# # name = df["name"].sort_values().values
# print(df)
# print(total_purchased)  

import pandas as pd
df1 = pd.read_csv("Data/data_1.csv")
df2 = pd.read_csv("Data/data_2.csv")
# merge_df = pd.merge(df1,df2,on="user_id")
merge_df = pd.merge(df1,df2,on="user_id")
print(merge_df)
# merge_df = pd.merge(df1,df2,on="user_id", how='left')
# print(merge_df)
# merge_df = pd.merge(df1,df2,on="user_id", how= 'right')
# print(merge_df)
merge_df = pd.merge(df1,df2,on="user_id",how='outer')
print(merge_df)
