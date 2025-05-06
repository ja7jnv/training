#!/usr/bin/env python


def gauss():
    print("Gauss method")

    import numpy as np

    # 配列を宣言
    T = np.ones(11)
    TN = np.ones(11)
    TK = np.ones(11)
    TIM = 0

    # 定数を宣言
    DT = 0.01
    DX = 0.1

    # 定数rの計算
    R = DT / DX / DX
    print("r ={:.6f}".format(R))

    # 初期値
    T[0] = 0
    T[10] = 0
    TN[0] = 0
    TN[10] = 0
    TK[0] = 0
    TK[10] = 0

    # 反復計算の準備
    for i in range(11):
        TK[i] = T[i]

    # 時間を進める
    j = 0
    while j < 4:
        j += 1

        print("")

        # 格子点iと番号の表示
        print("i        ", end="")
        for i in range(11):
            print("{:>8}".format(i), end="  ")

        print("        ε max")

        # 反復条件の設定
        MAXEPS = 0.01
        k = 0
        while MAXEPS > 0.001:
            k += 1

            print("k ={:>3}".format(k), "    ", end=" ")
            print("{:.6f}".format(T[0]), end="  ")

            MAXEPS = 0
            for i in range(1, 10):
                # Gauss-Seidelの反復法
                T[i] = (
                    R / (1 + 2 * R) * (T[i - 1] + TK[i + 1]) + 1 / (1 + 2 * R) * TN[i]
                )
                EPS = abs((T[i] - TK[i]) / T[i])

                if EPS > MAXEPS:
                    MAXEPS = EPS

                print("{:.6f}".format(T[i]), end="  ")

            print("{:.6f}".format(T[10]), "     ", end=" ")
            print("{:.6f}".format(MAXEPS))

            # 近似値の更新
            for i in range(11):
                TK[i] = T[i]

        k = 0

        # 時刻を記述、収束した近似値を現在時刻に置き換え
        TIM += DT

        print("t = {:.4f}".format(TIM), end="  ")
        for i in range(11):
            TN[i] = T[i]
            TK[i] = T[i]
            print("{:.6f}".format(TN[i]), end="  ")

        print("     {:.6f}".format(MAXEPS))


if __name__ == "__main__":
    gauss()
