#!/usr/bin/env python

#import matplotlib,pyplot as plt

def main():
    print("Jacobi method")

    #定数を指定
    DT = 0.01
    DX = 0.1

    #変数rの計算
    R = DT / DX**2
    print("r ={:.6f}".format(R))

    #配列に値を代入
    TIM = 0

    #初期値
    T = [1] * 11
    TN = [1] * 11
    TK = [1] * 11

    #境界条件
    T[0] = 0
    T[10] = 0
    TN[0] = 0
    TN[10] = 0
    TK[0] = 0
    TK[10] = 0

    #反復計算の準備
    for i in range(0, 11):
        TK[i] = T[i]

    #時間を進める
    j = 0
    while j < 1:
        j = j + 1

        #格子点iと番号の表示
        print("          ", end="")
        for i in range(0, 11):
            print("{:>8}".format(i), end=" ")
        print("        ε max")

        #反復条件の設定
        MAXEPS = 0.01
        k = 0
        while MAXEPS > 0.001:    # ε = 10**(-3)
            k = k + 1
            print("k ={:>3}".format(k), "    ", end=" ")
            print("{:.6f}".format(T[0]), end=" ")

            MAXEPS = 0
            for i in range(1,10):
                #Jacobiの反復法
                T[i] = R/(1+2*R) * (TK[i-1] + TK[i+1]) + 1/(1+2*R)/TN[i]
                EPS = abs((T[i] - TK[i]) / T[i])

                if EPS > MAXEPS:
                    MAXEPS = EPS

                print("{:.6f}".format(T[i]), end=" ")

            print("{:.6f}".format(T[10]), "     ",end=" ")
            print("{:.6f}".format(MAXEPS))

            for i in range(1,10):
                TK[i] = T[i]

        k = 0

        #時刻を記述、収束した近似値を現在時刻の値に置き換える
        TIM = TIM + DT

        print("")
        print("t = {:.4f}".format(TIM), "", end=" ")

        for i in range(0,11):
            TN[i] = T[i]
            TK[i] = T[i]
            print("{:.6f}".format(TN[i]), end=" ")
        
        print("      {:.6f}".format(MAXEPS))



if __name__ == "__main__":
    main()
                                