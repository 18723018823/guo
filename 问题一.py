#合并附件一附件二
import pandas as pd
dataframe1=pd.read_excel('附件1.xlsx')
dataframe2=pd.read_excel('附件2.xlsx')
merged_data = pd.merge(dataframe1, dataframe2, on='单品编码',how='right')
merged_data['销售日期']=pd.to_datetime(merged_data['销售日期'])

#统计单品、品类的日度月度销售量
sales_datam=pd.DataFrame()
sales_datam=merged_data.groupby(['销售年月', '单品名称'])['销量(千克)'].sum().unstack(fill_value=0)
sales_datal=pd.DataFrame()
merged_data['销售年月']=merged_data['销售日期'].dt.strftime('%Y-%m')
sales_datalm=merged_data.groupby(['销售年月','分类名称'])['销量(千克)'].sum().unstack(fill_value=0)
sale_total=sales_datalT.sum()
sale_total=sale_total.T
sales_data.to_csv('单品日销售量T.csv',encoding='utf-8')
sales_datal.to_csv('分类日销售量T.csv',encoding='utf-8')
sale_total.to_csv('总销售量T.csv',encoding='utf-8')

#Spearman相关系数分析
df1=pd.read_csv('分类日销售量T.csv')
df2020=df1[(df1['销售日期'] >= '2020-07-01') & (df1['销售日期'] <= '2021-06-30')]
df2021=df1[(df1['销售日期'] >= '2021-07-01') & (df1['销售日期'] <= '2022-06-30')]
df2022=df1[(df1['销售日期'] >= '2022-07-01') & (df1['销售日期'] <= '2023-06-30')]
df2020.to_csv('2020lei.csv',encoding='utf-8')
df2021.to_csv('2021lei.csv',encoding='utf-8')
df2022.to_csv('2022lei.csv',encoding='utf-8')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
print(df2020)
corr_ma2020, _ = spearmanr(df2020)
plt.figure(figsize=(8, 6))
sns.heatmap(corr_ma2020, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap2020')

corr_ma2021, _ = spearmanr(df2021)
plt.figure(figsize=(8, 6))
sns.heatmap(corr_ma2021, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap2021')

corr_ma2022, _ = spearmanr(df2022)
plt.figure(figsize=(8, 6))
sns.heatmap(corr_ma2022, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap2022')
plt.show()

sumdf=pd.DataFrame()
dfd1=pd.read_csv('单品日销售量.csv')
sumdf['总销量']=dfd1.sum(axis=1)
sumdf=pd.concat([dfd1['单品名称'],sumdf ], axis=1)
sumdf.to_csv('单品汇总.csv')
sumdf=sumdf.sort_values(by='总销量', ascending=False)
summaxdf=sumdf
summaxdf.to_csv('单品销售量排行.csv')
dfm1=pd.read_csv('分类月销售量.csv')
dfm2=pd.read_csv('单品月销售量.csv')
huise=pd.concat([dfm1,dfm2],axis=1)
huise.to_csv('灰色关联分析.csv')
list_sale=[]
list_sale=sumdf['单品名称']
no_sale=dataframe1[~dataframe1['单品名称'].isin(list_sale)]
no_sale['单品名称']