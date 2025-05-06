#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt


def implicit(method_numer):
    METHOD = ("Jacobi", "Gauss-Seidel", "SOR")
    print("Method : ", METHOD[method_numer])

    # 配列を宣言
    T = np.ones(11)
    TN = np.ones(11)
    TK = np.ones(11)
    TIM = 0

    # 定数を宣言
    DT = 0.01
    DX = 0.1
    W = 1.2

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
                if method_numer == 0:   # この方法は美しくない（要改善）
                    # Jacobi の反復法
                    T[i] = (
                        R / (1 + 2 * R) * (TK[i - 1] + TK[i + 1]) + 1 / (1 + 2 * R) * TN[i]
                    )
                elif method_numer == 1:
                    # Gauss-Seidel の反復法
                    T[i] = (
                        R / (1 + 2 * R) * (T[i - 1] + TK[i + 1]) + 1 / (1 + 2 * R) * TN[i]
                    )
                elif method_numer == 2:
                    # SOR の反復法
                    T[i] = (
                    	W * (R / (1 + 2 * R) * (T[i - 1] + TK[i + 1]) + 1 / (1 + 2 * R) * TN[i]) - (W - 1) * TK[i]
                    )
                else:
                    print("Internal error (101).")
                    sys.exit(-1)

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

        # 折れ線グラフで表示
        plt.plot(T, label="t={:.4f}".format(TIM))

        # 時刻を記述、収束した近似値を現在時刻に置き換え
        TIM += DT

        print("t = {:.4f}".format(TIM), end="  ")
        for i in range(11):
            TN[i] = T[i]
            TK[i] = T[i]
            print("{:.6f}".format(TN[i]), end="  ")

        print("     {:.6f}".format(MAXEPS))

    # 表題
    plt.legend()
    plt.title("{:s} method  (r={:.2f})".format(METHOD[method_numer], R))
    plt.xlabel("lattice point")
    plt.ylabel("τ")
    plt.show()


if __name__ == "__main__":
    args = sys.argv
    arguments = len(args)
    if arguments < 2:
        while True:
            argument_1 = input(
                "jacobi=1, gauss=2, SOR=3, 9:exit\n Select method : "
            )
            if (argument_1 == "1") or \
               (argument_1 == "2") or \
               (argument_1 == "3") or \
               (argument_1 == "9"):
                break
            else:
                continue
        method = int(argument_1)

    elif arguments > 2:
        print('Arguments are too long')
        method = 9

    else:
        if "jacobi" in args[1]:
            method = 1
        elif "gauss" in args[1]:
            method = 2
        elif "sor" in args[1]:
            method = 3
        else:
            print("\'{:s}\'".format(args[1]), "is wrong method.")
            print("Possible types are \'jacobi\', \'gauss\', or \'sor\'.")
            method = 9

    if method == 9:
        sys.exit()

    implicit(method-1)
