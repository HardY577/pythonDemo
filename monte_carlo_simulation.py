import numpy as np
def monte_carlo_simulation(S0, r, sigma, T, n_steps):
  """
  蒙特卡洛模拟几何布朗运动
  参数：
    S0: 初始股票价格
    r: 无风险利率
    sigma: 波动率
    T: 模拟时间
    n_steps: 模拟步数
  返回：
    模拟路径
  """
  # 初始化模拟路径
  path = [S0]
  # 生成随机增量
  dt = T / n_steps
  for _ in range(n_steps):
    dWt = np.random.normal(0, np.sqrt(dt))
    St = path[-1] * np.exp((r - sigma**2 / 2) * dt + sigma * dWt)
    # 更新模拟路径
    path.append(St)
  return path