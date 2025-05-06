import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_polar_curve(a):
    """パラメータ a を持つ極座標曲線のデータを生成する関数"""
    theta = np.linspace(0, 2*np.pi, 500)
    r = 1 / (1 - a * np.cos(theta))

    # r が負または無限大になる点をマスクする
    r_masked = np.ma.masked_where((r <= 0) | (np.isinf(r)), r)
    theta_masked = np.ma.masked_where((r <= 0) | (np.isinf(r)), theta)

    return theta_masked, r_masked

def update(frame):
    """アニメーションの各フレームを更新する関数"""
    ax.clear()
    a = np.linspace(0, 1.5, num_frames)[frame]
    theta, r = create_polar_curve(a)
    ax.plot(theta, r)
    ax.set_title(f'Polar Curve: r = 1 / (1 - {a:.2f} cosθ)')
    ax.set_rticks([0.5, 1, 1.5, 2])  # r軸の目盛りを設定
    ax.grid(True)

def on_press(event):
    """キーが押されたときのイベント処理関数"""
    global running
    if event.key == ' ':
        if running:
            ani.event_source.stop()
            running = False
        else:
            ani.event_source.start()
            running = True

# アニメーションの設定
num_frames = 150
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=100)

# スペースキー押下時のイベントハンドラを設定
running = True
fig.canvas.mpl_connect('key_press_event', on_press)

plt.show()
