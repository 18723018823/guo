import pandas as pd
dataframe1=pd.read_excel('附件1.xlsx')
dataframe2=pd.read_excel('附件3.xlsx')
merged_data = pd.merge(dataframe1, dataframe2, on='单品编码',how='right')
print(merged_data)
# merged_data['销售日期']=pd.to_datetime(merged_data['销售日期'])
sales_datal=pd.DataFrame()
sales_datal=merged_data.groupby(['日期', '分类名称'])['批发价格(元/千克)'].sum().unstack(fill_value=0)
sales_datalT=sales_datal.T
# sales_datT.to_excel('单品日销售量_2.xlsx')
sales_datal.to_excel('分类批发量_1.xlsx')
# sale_total.to_excel('总销售量_1.xlsx')
merged_data.to_excel('merge.xlsx')