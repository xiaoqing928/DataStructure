'''
给定一个有N*M的整型矩阵matrix和一个整数K，
matrix的每一行和每一 列都是排好序的。实现一个函数，判断K是否在matrix中
'''
import numpy as np
l = [0, 1, 2, 5 ,2, 3, 4, 7, 4,
4, 4, 8, 5, 7, 7, 9]
mat = np.array(l).reshape(4,4)
# print(mat)

def searchNumber(mat, num):
    endr = len(mat) - 1
    endc = len(mat[0]) - 1
    r, c = 0, endc
    count = 0
    while r != endr or c != 0:
        if mat[r][c] == num:
            return count
        elif mat[r][c] > num:
            c -= 1
            count += 1
        else:
            r += 1
            count += 1
    return count
r = searchNumber(mat, 4)
print(r)