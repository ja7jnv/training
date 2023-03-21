#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

def	crank_nicolson():
    print("Method : Crank-Nicolson")

    #配列を宣言&初期値の設定
    T = np.ones(11)
    TN = np.ones(11)
    TK = np.ones(11)
    TIM = 0

	#定数を指定
    DT = 0.01
    DX = 0.1

	#変数rの計算
    R = DT / (DX**2)
    print("r ={:.6f}".format(R))

	#境界条件
    T[0] = 0
    T[10] = 0
    TN[0] = 0
    TN[10] = 0
    TK[0] = 0
    TK[10] = 0

	#反復計算の準備
    for i in range(11):
        TK[i] = T[i]

	#時間を進める
    j = 0
    while j < 5:
        j = j + 1
        TIM = TIM + DT

        print("")

        #格子点iと番号の表示
        print("i        ", end="")
        for i in range(11):
            print("{:>8}".format(i), end="  ")

        print("        ε max")
		
        #反復条件の設定
        MAXEPS = 0.01
        k = 0
        while MAXEPS > 0.001:
            k = k + 1

            print("k ={:>3}".format(k), "    ", end=" ")
            print("{:.6f}".format(T[0]), end="  ")

            MAXEPS = 0
			
            for i in range(1, 10):
                #Jacobiの反復法
                #T[i] = R / (1 + 2 * R) * (TK(i - 1) + TK(i + 1)) + 1 / (1 + 2 * R) * TN(i)

                #クランク・ニコルソン法
                T[i] = (
					R / 2 / (1 + R) * (TK[i - 1] + TK[i + 1]) + 1 / 2 / (1 + R) * (R * TN[i - 1] + 2 * (1 - R) * TN[i] + R * TN[i + 1])
                    )
                EPS = abs((T[i] - TK[i]) / T[i])

                if EPS > MAXEPS:
                    MAXEPS = EPS
				
                print("{:.6f}".format(T[i]), end="  ")

            print("{:.6f}".format(T[10]), "     ", end=" ")
            print("{:.6f}".format(MAXEPS))


			#近似値の計算
            for i in range(11):
                TK[i] = T[i]

        # 折れ線グラフで表示
        plt.plot(T, label="t={:.4f}".format(TIM))
			
		#時刻を記述、収束した近似値を現在時刻に置き換え
        print("t = {:.4f}".format(TIM), end="  ")
		
        for i in range(11):
            TN[i] = T[i]
            TK[i] = T[i]
            print("{:.6f}".format(T[i]), end="  ")

        print("     {:.6f}".format(MAXEPS))

    # 表題
    plt.legend()
    plt.title("{:s} method  (r={:.2f})".format("Crank-Nicolson", R))
    plt.xlabel("lattice point")
    plt.ylabel("τ")
    plt.show()

if __name__ == "__main__":
	crank_nicolson()
