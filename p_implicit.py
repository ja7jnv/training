#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class IterativeMethod(ABC):
    @abstractmethod
    def iterate(self, T, TK, TN, R, W):
        pass


class JacobiMethod(IterativeMethod):
    def iterate(self, T, TK, TN, R, W):
        for i in range(1, 10):
            T[i] = R / (1 + 2 * R) * (TK[i - 1] + TK[i + 1]) + 1 / (1 + 2 * R) * TN[i]
        return T


class GaussSeidelMethod(IterativeMethod):
    def iterate(self, T, TK, TN, R, W):
        for i in range(1, 10):
            T[i] = R / (1 + 2 * R) * (T[i - 1] + TK[i + 1]) + 1 / (1 + 2 * R) * TN[i]
        return T


class SORMethod(IterativeMethod):
    def iterate(self, T, TK, TN, R, W):
        for i in range(1, 10):
            T[i] = W * (R / (1 + 2 * R) * (T[i - 1] + TK[i + 1]) + 1 / (1 + 2 * R) * TN[i]) - (W - 1) * TK[i]
        return T


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


