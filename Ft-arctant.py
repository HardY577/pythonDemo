import numpy as np
import matplotlib.pyplot as plt

# 定义函数 F(t)
def F(t):
    return 100/np.pi * np.arctan(t) + 100/2

# 定义 t 的范围
t = np.linspace(-10, 10, 500)

# 计算对应的 F(t) 值
f_t = F(t)

# 绘制图像
plt.figure(figsize=(8,6))
plt.plot(t, f_t, label=r'$F(t) = \frac{100}{\pi} \arctan(t) + 50$', color='b')
plt.title(r'Plot of $F(t)$', fontsize=16)
plt.xlabel('t', fontsize=14)
plt.ylabel(r'$F(t)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best')
plt.show()
