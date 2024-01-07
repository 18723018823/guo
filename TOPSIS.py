import pandas as pd
import numpy as np

# 读取数据
df = pd.read_csv(
data = df.iloc[:, 2:6]

# 计算每个指标的最小值、最大值和范围
min_values = data.min()
max_values = data.max()
ranges = max_values-min_values

# 正向化指标 ,第四列（标准差）进行了反向化处理，以将不利指标的数值越小越好的特征转化为越大越好的特征
data_normalized = data.copy()
data_normalized.iloc[:, 0] = (data.iloc[:, 0] - min_values[0]) / ranges[0]
data_normalized.iloc[:, 1] = (data.iloc[:,1] - min_values[1]) / ranges[1]
data_normalized.iloc[:, 2] = (data.iloc[:, 2] - min_values[2]) / ranges[2]
data_normalized.iloc[:, 3] = (max_values[3] - data.iloc[:, 3]) / ranges[3]


# 将已经正向化的指标标准化
z=data_normalized.apply(lambda x:x/np.sqrt(sum(x**2)))
if(data_normalized<0).sum().sum()<0:
    z=data_normalized.apply(lambda x:(x-x.min())/(x.max()-x.min()),axis=0)

#   熵权法计算信息熵e,信息效用值d,熵权w
p=z/z.sum()
e=np.nan_to_num(-p*np.log(p)).sum(axis=0)/np.log(len(p))
d=1-e

# 计算每个指标的权重
w=d/d.sum()

# 熵权法计算最终得分
D_positive=(((z.max()-z)**2)*w).sum(axis=1)**0.5
D_negative=(((z.min()-z)**2)*w).sum(axis=1)**0.5
S=D_negative/(D_positive+D_negative)
score=pd.DataFrame((S/S.sum()).sort_values(ascending=False),columns=["最终得分"])

# 将结果输出到CSV文件中
result = pd.DataFrame({
    "指标": [f"指标{i+1}" for i in range(data.shape[1])],
    "信息熵": e,
    "信息效用值": d,
    "权重": w
})
suoyin=df.iloc[:,0:2]
results=pd.concat([result,suoyin,score],axis=1)
