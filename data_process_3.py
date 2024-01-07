# 问题2
import pandas as pd

# 读取两个Excel文件
df_sales = pd.read_excel('附件2.xlsx')
df_categories = pd.read_excel('附件1.xlsx')

# 合并两个数据集以获取单品的分类信息
df_merged = df_sales.merge(df_categories, on='单品编码')

# 计算销售额（销售量 * 单价）
df_merged['销售额'] = df_merged['销量(千克)'] * df_merged['销售单价(元/千克)']

# 步骤 2：计算每个分类在每一天的总销售量和总销售额
category_day_totals = df_merged.groupby(['分类名称', '销售日期'])[['销量(千克)', '销售额']].sum().reset_index()

# 步骤 3：计算每个单品在其所属分类中的销售量占比
df_merged['销售量占比'] = df_merged.groupby(['分类名称', '销售日期'])['销量(千克)'].apply(lambda x: x / x.sum())

# 步骤 4：计算每个单品的加权单价
df_merged['加权单价'] = df_merged['销售单价(元/千克)'] * df_merged['销售量占比']

# 步骤 5：计算每个分类在每一天的加权单价
category_day_weighted_prices = df_merged.groupby(['分类名称', '销售日期'])['加权单价'].sum().reset_index()

# 打印结果
# print(category_day_weighted_prices)
# df_merged['分类单价']=category_day_weighted_prices
# 合并分类单价信息到 df_merged 中
# df_merged = df_merged.merge(category_day_weighted_prices, on=['分类名称', '销售日期'], how='left')
#
# df_merged.to_excel('no2.xlsx')
category_day_weighted_prices.to_excel('n03.xlsx')
