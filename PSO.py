mport numpy as np
import matplotlib.pyplot as plt
from pyswarm import pso


# 目标函数
def objective(x):
    P, S = x
    beta = 0.5  # 自适应惯性权重
    C_dot = 100  # 常数C_dot
    mu_p = 0.1  # mu(p)
    sigma_p = 0.2  # sigma(p)

    # 计算目标函数值
    term1 = (P - (1 - beta) * C_dot) * S
    term2 = P / ((1 + (P - mu_p) / sigma_p) ** 2)
    return - (term1 + term2)  # 最大化问题，取负号


# 约束条件
def constraint(x):
    P, S = x
    N_max = 100  # N_max的值
    M_max = 200  # M_max的值
    beta = 0.5  # 自适应惯性权重
    delta = 0.5  # 非对称学习因子

    # 定义约束条件
    constraints = [
        S - N_max,  # 0 <= S <= N_max
        S - M_max * (1 - beta),  # 0 <= S <= M_max * (1 - beta)
        delta - 1  # 0 < delta < 1
    ]
    return constraints


# 定义搜索范围（上下界）
lb = [0, 0]  # 下界
ub = [100, 100]  # 上界

# 记录迭代过程中的损失值
loss_history = []


# 迭代函数
def callback(xk, convergence):
    # 计算当前迭代的损失值并记录
    current_loss = -objective(xk)  # 因为目标函数是最大化问题，所以取负号
    loss_history.append(current_loss)


# 使用PSO算法求解
xopt, fopt = pso(objective, lb, ub, f_ieqcons=constraint, swarmsize=100, maxiter=100, callback=callback)

# 输出最优解
print("最优解：", xopt)
print("最优目标函数值：", -fopt)  # 因为目标函数是最大化问题，所以取负号

# 绘制损失值降低图
plt.figure()
plt.plot(loss_history)
plt.title('Loss History')
plt.xlabel('Iteration')
plt.ylabel('Loss Value')
plt.show()