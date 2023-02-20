#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt


def implicit(method):
    m = ("Jacobi", "Gauss-Seidel", "SOR")   
    print("method : ", m[method])



if __name__ == "__main__":
    args = sys.argv
    l = len(args)
    if l < 2:
        while True:
            method = input("jacobi=1, gauss=2, SOR=3, 9:exit\n Select method : ")
            if (method == "1") or (method == "2") or (method == "3") or (method == "9"):
                break
            else:
                continue
        method = int(method)

    elif l > 2:
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
            print("\'{:s}\'".format(args[1]),"is wrong method.")
            print("Possible types are \'jacobi\', \'gauss\', or \'sor\'.")
            method = 9

    if method == 9: 
        sys.exit()

    implicit(method-1)
