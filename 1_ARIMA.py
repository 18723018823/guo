import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.arima.model import ARIMA
from sklearn import metrics
import matplotlib as mpl
mpl.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# 读取数据（可选择14-10、20-35，25-62三个文件）
Data=pd.read_csv('./14-10.csv')
Data1=Data.iloc[:,1]
# 差分
D_data = Data1.diff( ).dropna()# 一阶差分
D_data2 = D_data.diff().dropna()# 二阶差分
# 绘制时序图
plt.figure()
plt.subplot(2,1,1)
Data1.plot()
plt.subplot(2,1,1)
D_data.plot()
plt.subplot(2,1,2)
D_data2.plot()
plt.show()
# ADF检验为单位根检验
print(u'原始序列的ADF检验结果为：',ADF(Data1))
print(u'一次差分序列的ADF检验结果为：',ADF(D_data))

print(u'二次差分序列的ADF检验结果为：',ADF(D_data2))

# 绘制自相关，偏自相关图
plt.figure()
plot_acf(Data1)
plt.savefig('ACF.png', dpi=300)
plot_pacf(Data1)
plt.savefig('PACF.png', dpi=300)
plt.show()

#  通过bic矩阵定阶
pmax = 10 # 一般不会大于10
qmax = 10 # 一般不会大于10
bic_matrix = []
for p in range(pmax):
    temp= []
    for q in range(qmax):
        try:
            temp.append(ARIMA(Data1,order=(p, 2, q)).fit().bic)
        except:
            temp.append(None)
        bic_matrix.append(temp)
bic_matrix = pd.DataFrame(bic_matrix)
p,q = bic_matrix.stack().idxmin()
print(u'BIC 最小的p值 和 q 值：%s,%s' %(p,q))

# 建立ARIMA模型
model = ARIMA(Data1,order=(p,2,q)).fit()
predictions_ARIMA_diff = pd.Series(model.fittedvalues, copy=True)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(predictions_ARIMA_diff,label="拟合数据")
plt.plot(Data1,label="原始数据")
plt.plot(model.forecast(31),label='预测数据')
plt.xlabel('日期',fontsize=12,verticalalignment='top')
plt.ylabel('货物',fontsize=14,horizontalalignment='center')
plt.legend()
plt.savefig('dpi.png', dpi=300)
plt.show()

# MSE计算 R平方计算
def mse(target, predict):
    return ((target - predict)**2).mean()
MSE = metrics.mean_squared_error(Data1,predictions_ARIMA_diff)
print(MSE)
delta = model.fittedvalues -Data1
score = 1 - delta.var() / Data1.var()
print('R^2：', score)

# 白噪声检验
# from statsmodels.stats.diagnostic import acorr_ljungbox
# print(u'差分序列的白噪声检验结果为：', acorr_ljungbox(D_data2, lags=1))

# 预测后31天
print(model.forecast(31))
# 我们将预测结果手动输入了__ARIMA.xlxs文件中
