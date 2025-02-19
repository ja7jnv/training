import numpy as np
import matplotlib.pyplot as plt

# 初期条件を設定する
x_min = 0  # xの最小値
x_max = 1  # xの最大値
nx = 100  # x方向の分割数
dx = (x_max - x_min) / nx  # x方向の刻み幅

# 境界条件を設定する
theta_min = 0  # θの最小値
theta_max = 1  # θの最大値

# 熱拡散方程式を解くためのアルゴリズムを実装する
alpha = 1  # 拡散係数
dt = 0.01  # 時間の刻み幅
t_max = 10  # 最大時間
nt = int(t_max / dt)  # 時間の分割数

# 初期条件を設定する
theta = np.zeros(nx)  # θを初期化する
for i in range(nx):
    theta[i] = 1.0  # 初期条件=1とする

# 時間発展させる
for t in range(nt):
    # 境界条件を設定する
    theta[0] = 0  # 境界条件=0とする
    theta[-1] = 0  # 境界条件=0とする

    # 熱拡散方程式を解く
    theta_new = np.zeros(nx)  # 新しいθを初期化する
    for i in range(1, nx - 1):
        theta_new[i] = theta[i] + alpha * dt / (dx ** 2) * (theta[i + 1] - 2 * theta[i] + theta[i - 1])
    theta = theta_new  # 新しいθを代入する

# 解いた熱拡散方程式をプロットする
plt.plot(theta)
plt.show()

