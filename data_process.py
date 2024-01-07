import pandas as pd

# 读取第一个Excel文件
df1 = pd.read_excel('单品日销售量.xlsx')

# 读取第二个Excel文件，包含单品名称和品类名称
df2 = pd.read_excel('附件1.xlsx')
# 将 '单品名称' 列的数据类型转换为字符串
# df1['单品名称'] = df1['单品名称'].astype(int)


# 使用merge函数将两个DataFrame合并
result_df = df1.merge(df2, on='单品名称', how='left')

# 将结果保存到新的Excel文件
result_df.to_excel('结果文件.xlsx', index=False)
