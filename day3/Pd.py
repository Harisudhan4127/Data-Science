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
# f_df = df[df['id']<10]
# print(f_df)
# # df.to_csv(r'C:\Users\STUDENT\Desktop\Python\Data\dummy.csv', index=False, header=True)


# Shop
import pandas as pd
df = pd.read_csv(r"C:\Users\STUDENT\Desktop\Python\Data\shop.csv")
total_purchased= df.groupby("purchased").agg({'cus_id' : 'count'})
print(total_purchased)