import pandas as pd

# 读取第一个Excel文件
df1 = pd.read_excel('花叶类.xlsx')
df2 = pd.read_excel('花菜类.xlsx')
df3 = pd.read_excel('辣椒类.xlsx')
df4 = pd.read_excel('食用菌.xlsx')
df5 = pd.read_excel('水生根茎类.xlsx')
df6 = pd.read_excel('茄类.xlsx')
df1T=df1.T
df2T=df2.T
df3T=df3.T
df4T=df4.T
df5T=df5.T
df6T=df6.T
# df1T.to_excel("花叶类1.xlsx")
df2T.to_excel("花菜类1.xlsx")
# df3T.to_excel("辣椒类1.xlsx")
# df4T.to_excel("食用菌1.xlsx")
# df5T.to_excel("水生根茎类1.xlsx")
# df6T.to_excel("茄类1.xlsx")
