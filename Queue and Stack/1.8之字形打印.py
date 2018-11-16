'''
给定一个矩阵matrix，按照“之”字形的方式打印这
个矩阵，例如： 1 2 3 4 5 6 7 8 9 10 11 12
“之”字形打印的结果为：1，2，5，9，6，3，4，7，10，11，8，12
'''

def printZ(mat, ar, ac, br, bc, fromup):
    if fromup == 1:
        while ar != br+1:
            print(mat[ar][ac])
            ar += 1
            ac -= 1
    else:
        while br != ar-1:
            print(mat[br][bc])
            br -= 1
            bc += 1

def mainZ(mat):
    ar, ac, br, bc = 0, 0, 0, 0
    endr = len(mat) - 1
    endc = len(mat[0]) - 1
    fromup = 0
    while ar != endr + 1:
        printZ(mat, ar, ac, br, bc, fromup)
        if ac < endc:
            ac += 1
        else:
            ar += 1
        if br < endr:
            br += 1
        else:
            bc += 1
        fromup = (fromup+1)%2

import numpy as np
mat = np.arange(1,17).reshape(4,4)
mainZ(mat)