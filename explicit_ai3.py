# 熱拡散方程式を解くプログラム

# 必要なモジュールをインポートする
import numpy as np

# 定数を設定する
alpha = 0.1  # 熱伝導率
L = 1  # 熱伝導距離
t_max = 1  # 最大時刻
dt = 0.01  # 時間刻み幅
dx = 0.01  # 空間刻み幅

# 格子点の数を求める
nx = int(L / dx) + 1  # x方向の格子点数
nt = int(t_max / dt) + 1  # t方向の格子点数

# 初期条件を設定する
theta = np.zeros(nx)  # 温度分布を0で初期化する
theta[int(nx / 2)] = 1  # 中央の格子点の温度を1にする

# 境界条件を設定する
theta[0] = 0  # 左端の格子点の温度を0にする
theta[-1] = 0  # 右端の格子点の温度を0にする

# 温度分布を求める
for t in range(1, nt):
    theta_new = np.zeros(nx)  # 温度分布を0で初期化する
    for i in range(1, nx-1):  # 内部の格子点を更新する
        theta_new[i] = theta[i] + alpha*dt*(theta[i+1] - 2*theta[i] + theta[i-1]) / dx**2
    theta = theta_new  # 温度分布を更新する

# 温度分布を出力する
for i in range(nx):
    print(f"{i*dx:.3f}\t{theta[i]:.3f}")

