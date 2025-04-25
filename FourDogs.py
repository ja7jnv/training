# Fourdogs.py 四匹の犬
"""
座標(x,y)=(0,0)に犬aがいる。
同じく(0,100)に犬b、(100,100)に犬c、及び(100,0)に犬ｄがいる。
犬aは犬bを、犬bは犬cを、犬cは犬dを、そして犬dは犬aを追いかける。
４匹が同時にt=0で相手の犬を追いかけ始める。
犬が追いかける速さは10/tである。
それぞれの犬の軌跡をアニメ化するコードを描け。
各犬の軌跡は色分けし、図の下部に時刻を表示をせよ。
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyArrowPatch

# 犬の初期位置
dog_a = np.array([0, 0], dtype=float)
dog_b = np.array([0, 100], dtype=float)
dog_c = np.array([100, 100], dtype=float)
dog_d = np.array([100, 0], dtype=float)

# 犬の速度
speed = 10

# 犬の色
colors = ['red', 'blue', 'green', 'orange']

# 犬の軌跡
trajectories = [[], [], [], []]

# 犬の初期位置を保存
trajectories[0].append(dog_a.copy())
trajectories[1].append(dog_b.copy())
trajectories[2].append(dog_c.copy())
trajectories[3].append(dog_d.copy())

# アニメーションの停止フラグ
animation_running = True

# 更新関数
def update(frame):
    global dog_a, dog_b, dog_c, dog_d, animation_running

    # 犬の位置を更新
    dog_a = move_dog(dog_a, dog_b)
    dog_b = move_dog(dog_b, dog_c)
    dog_c = move_dog(dog_c, dog_d)
    dog_d = move_dog(dog_d, dog_a)

    # 犬が追いついたらアニメーションを停止
    Stop_conditions = 1e-2

    if (
        np.linalg.norm(dog_a - dog_b) < Stop_conditions or
        np.linalg.norm(dog_a - dog_b) < Stop_conditions or
        np.linalg.norm(dog_b - dog_c) < Stop_conditions or
        np.linalg.norm(dog_c - dog_d) < Stop_conditions or
        np.linalg.norm(dog_d - dog_a) < Stop_conditions ):

        ani.event_source.stop()
        animation_running = False
        return

    # 軌跡を保存
    trajectories[0].append(dog_a.copy())
    trajectories[1].append(dog_b.copy())
    trajectories[2].append(dog_c.copy())
    trajectories[3].append(dog_d.copy())

    # 描画
    ax.clear()
    ax.set_xlim(-10, 110)
    ax.set_ylim(-10, 110)
    ax.set_title(f"Time: {frame * dt:.2f} seconds")
    for i in range(4):
        trajectory = np.array(trajectories[i])
        ax.plot(trajectory[:, 0], trajectory[:, 1], color=colors[i], label=f'Dog {i+1}')
        ax.scatter(trajectory[-1][0], trajectory[-1][1], color=colors[i])
        if len(trajectory) > 1:
            ax.add_patch(FancyArrowPatch(trajectory[-2], trajectory[-1], color=colors[i], arrowstyle='->', mutation_scale=15))
    ax.legend(loc='upper right')

# 犬の移動関数
def move_dog(dog_pos, target_pos):
    direction = target_pos - dog_pos
    distance = np.linalg.norm(direction)
    if distance == 0:
        return dog_pos
    direction /= distance
    new_pos = dog_pos + direction * speed * dt  # 時間 dt を基準に速度を計算
    return new_pos

# 一時停止・再開の切り替え
def toggle_animation(event):
    global animation_running
    if event.key == ' ':
        if animation_running:
            ani.event_source.stop()
        else:
            ani.event_source.start()
        animation_running = not animation_running

# アニメーションの設定
fig, ax = plt.subplots()
ax.set_xlim(-10, 110)
ax.set_ylim(-10, 110)
time_text = ax.text(5, 105, '', fontsize=12)

# アニメーションのフレーム数
num_frames = 1000
# 時間の刻み
dt = 0.1

# アニメーションの作成
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=100, blit=False)

# キーボードイベントを登録
fig.canvas.mpl_connect('key_press_event', toggle_animation)

# アニメーションの表示
plt.show()
