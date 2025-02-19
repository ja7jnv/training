import numpy as np

# 熱伝導率
alpha = 0.1

# 求める区間（空間）とステップ数
L = 1.0
Nx = 100
dx = L / Nx

# 求める時間とステップ数
T = 0.1
Nt = 100
dt = T / Nt

# 初期条件
x = np.linspace(0, L, Nx+1)
theta = np.ones(Nx+1)

# 境界条件
theta[0] = 0
theta[-1] = 0

# 時間方向に解を進める
for n in range(Nt):
    # 新しい解を求める
    theta_new = np.zeros(Nx+1)
    for i in range(1, Nx):
        theta_new[i] = theta[i] + alpha * dt / dx**2 * (theta[i+1] - 2*theta[i] + theta[i-1])
    # 境界条件
    theta_new[0] = 0
    theta_new[-1] = 0
    # 新しい解を反映
    theta = theta_new

# 解をプロットする
import matplotlib.pyplot as plt
plt.plot(x, theta)
plt.show()

