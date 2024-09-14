# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:43:06 2020

@author: 10913
"""


import numpy as np
import matplotlib.pyplot as plt

from monte_carlo_simulation import monte_carlo_simulation


"""
几何布朗运动:
    St=S0*exp(ut)
    St=S0*exp(u t+o e sqrt(dt))

    St=S0*exp(a t+b z)

    - S0 是初始价格
    - a 是漂移率（长期的平均收益率）
    - b 是波动率（价格变化的波动大小）
    - z 是随机扰动项，遵循正态分布

程序的逻辑：
1、初始化模拟路径：设置模拟路径的起点为当前股票价格 S0。
2、生成随机增量：根据几何布朗运动的增量分布，生成一个随机增量 dWt。
3、更新模拟路径：根据几何布朗运动的微分方程，更新模拟路径：S(t+dt) = S(t) * exp((r - σ^2/2) * dt + σ * dWt)
4、重复步骤 2 和 3：重复以上步骤，直到模拟路径达到预定的时间点。

"""
D = 200  # 250个交易日
T = 1.0  # 总时间1年
dt = T / D  # 单位时间

# 资产价格矩阵的初始化
s0 = 4  # 初始价格
i = 3  # 要模拟的价格路径数量
st = np.zeros((i, D))  # 创建一个 (i, D) 的矩阵，用于存储不同路径下的资产价格
st[0] = (
    s0  # st 是存储每条路径在每个时间点的价格的矩阵，大小为 (i, D)，即 3 条路径、每条路径 200 个时间点的价格。
)

# GBM参数设置
sigma = 0.0001  # 波动率，代表价格的波动幅度
r = sigma**2 / 2  # 漂移率，代表价格的长期平均增长率
n = round(T / dt)  # 时间维度，实际上等于 D


"""
另一种写法
S=np.zeros((M+1,I))

S[0]=S0 #定义S[0]=S0

for t in range(1,M+1):

    S[t]=S[t-1]*np.exp(mean*dt+sigma*np.sqrt(dt)*np.random.standard_normal(I))

"""

# 绘制每条路径
plt.subplot(212)  # 创建一个图形窗口
for g in range(1, i):
    t = np.linspace(0, T, n)  # 在 [0, T] 之间生成 n 个等间距的时间点
    e = np.random.standard_normal(size=n)  # 生成 n 个标准正态分布的随机数
    z = np.cumsum(e) * np.sqrt(dt)  # 对随机数累加，并乘以 sqrt(dt) 得到 z
    x = r * t + sigma * z
    # 根据时间 t 和随机扰动 z 计算的过程 x
    st[g] = st[0] * np.exp(z)

    plt.plot(t, st[g], label="st" + str(g))

# 显示图形
plt.legend()
plt.show()
