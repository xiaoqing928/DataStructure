'''
   简单的不考虑分布式
   分布式时考虑并查集结构
'''

import numpy as np

island = np.mat([[1,0,0,0,0],
                 [1,0,1,0,1],
                 [0,1,1,0,1],
                 [1,0,1,0,1]])
# print(island[0,0])

#感染函数
def infect(mat, m, n, i, j):
    '''
    :param mat:矩阵
    :param m: 矩阵的行
    :param n: 矩阵的列
    :param i: 第i行
    :param j: 第j行
    :return: None
    '''
    if i >= m or j >= n or i < 0 or j < 0 or mat[i, j] != 1:
        return 0
    mat[i, j] = 2
    #上
    infect(mat, m, n, i - 1, j)
    #下
    infect(mat, m, n, i + 1, j)
    #左
    infect(mat, m, n, i, j - 1)
    #右
    infect(mat, m, n, i, j + 1)

#遍历矩阵
def research(mat):
    m, n = mat.shape
    res = 0
    for i in range(m):
        for j in range(n):
            if mat[i,j] == 1:
                res += 1
                infect(mat, m, n, i, j)
    return res

r = research(island)
print(r)