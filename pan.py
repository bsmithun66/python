import pandas as pd
# # s = pd.Series([10,20,30],index=['a','b','d'])
# # print(s)
# # print(s['b'])
# # print(s.values)

# data = {
#     "Name": ["Alice","Bob","Charlie","David"],
#     "Age": [19,20,21,22],
#     "Score": [50,55,70,90]
# }
# df = pd.DataFrame(data,index=['a','b','c','d'])
# print(df)
# #row access using iloc[] -> access row by integer 
# print(df.iloc[1])
# #row access using loc[] -> access row by index label 
# print(df.loc['d'])
# #masking the datafrrame
# print(df[df["Score"]>55])
# df["Grade"]= ["B","C","A","O"]#adds new column
# print(df)
# df.drop("Age",axis=1,inplace=True)#axis refers to row 
# print(df)
# df.rename(columns={"Score":"Marks"},inplace=True)
# print(df)

# import numpy as np
# df1 = pd.DataFrame({
#     "Food":["Pizza","Burger","Noodels",None],
#     "Pirce":[20,40,50,np.nan]
# })
# print(df1.isnull())
# df1.fillna("xyz")
# print(df1)
# df1.dropna(inplace=True)
# print(df1)

# #aggregate function
# print(df.describe())
# print(df.mean(numeric_only=True))
# print(df.groupby("Grade")["Marks"].mean())

# df2 = pd.read_csv("currency.csv")
# print(df2.head(10))#first 10 rows
# print(df2.tail(9))#last 9 rows

# df.to_csv("Student.csv",index=False)

# print(df[0:2])#slicing
# df.set_index("Name",inplace=True)
# print(df)
# df.reset_index(inplace=True)
# print(df)

# s = pd.Series([10,20,30],index=['a','b','d'])
# print(s)
# print(s['b'])
# print(s.values)

# s1=pd.Series({'x':5,'y':10,'z':15})
# print(s1.index)
# print(s.index)
# print(s1.dtype)
# print(s1.size)
# print(s1.shape)
# print(s1[['x','z']])
# s1['x']=20
# print(s1)
# s1['w']=24
# print(s1)
# s1.drop('y',inplace=True)
# print(s1)

# x=pd.Series([10,20,30])
# print(x+2)
# print(x*10)
# print(x**2)
# print(x[x>20])

# y= pd.Series([10,None,30,np.nan,40,70])
# print(y.isnull())
# y.dropna(inplace=True)
# print(y)

# z=pd.Series([10,20,30,40,50])
# print(z.describe())
# print(z.mean())
# print(z.max(),z.min())
# print(z.std())#std deviation
# print(z.sum())

# name = pd.Series(["alice","bob","charile","david"])
# print(name.str.upper())
# print(name.str.capitalize())
# print(name.str.contains("a"))

# x1 = pd.Series([30,40,50,90], index = ['d','b','a','c'])
# print(x1.sort_index())
# print(x1.sort_values())
# print(x1.rank())

y1 = pd.Series([5,15,25],index=['b','c','d'])
y2 = pd.Series([10,20,30],index=['a','b','c'])
print(y1+y2)