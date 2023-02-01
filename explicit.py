#!/usr/bin/env python

import matplotlib.pyplot as plt


def main():

    print("Explicit method")

    # 定数を指定
    DT = 0.0025
    DX = 0.1

    # 変数rの計算
    R = DT / (DX) ** 2
    print("r = ", R)

    # 初期条件 T[0]...T[10] = 1
    TIM = 0
    T = [1] * 11
    TT = [0] * 11

    # 境界条件
    T[0] = 0
    TT[0] = 0
    T[10] = 0
    print("T  = ", T, "\nTT = ", TT, "\n")

    # 格子点iと番号の表示
    print("          ", end="")

    for i in range(0, 11):
        print("      ", i, end=" ")

    print("")

    # 時間を進める
    for j in range(11):
        TIM = TIM + DT

        # 時間を表示
        print("t = {:.4f}".format(TIM), " ", "{:.6f}".format(TT[0]), end=" ")

        # 陽解法の公式
        for i in range(1, 10):
            TT[i] = R * (T[i - 1] + T[i + 1]) + (1 - 2 * R) * T[i]

            # 計算結果を表示
            print("{:.6f}".format(TT[i]), end=" ")

        print("{:.6f}".format(TT[10]))

        # 折れ線グラフで表示
        plt.plot(TT, label="t={:.4f}".format(TIM))

        # 解を置き換え、現在時刻とする
        for i in range(1, 10):
            T[i] = TT[i]

    # 表題
    plt.legend()
    plt.title("Explicit method  (r={:.2f})".format(R))
    plt.xlabel("lattice point")
    plt.ylabel("τ")
    plt.show()


if __name__ == "__main__":
    main()
