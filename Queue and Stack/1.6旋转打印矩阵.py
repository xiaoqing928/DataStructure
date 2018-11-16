'''
看左神视频里的介绍，见笔记本的总结
'''


def mainD(mat):
    tr = 0
    tc = 0
    dr = len(mat) - 1
    dc = len(mat[0]) - 1
    while tr <= dr and tc <= dc:
        printEdge(mat,tr,tc,dr,dc)
        tr += 1
        tc += 1
        dr -= 1
        dc -= 1

def printEdge(mat, tr, tc, dr, dc):
    '''
    :param mat:矩阵 
    :param tr: 左行
    :param tc: 左列
    :param dr: 右行
    :param dc: 右列
    :return: 
    '''
    #只有一行
    if tr == dr:
        for i in range(tc, dc+1):
            print(mat[tr][i])
    #只有一列
    elif tc == dc:
        for i in range(tr, dr+1):
            print(mat[i][tc])
    else:
        curR = tr
        curC = tc
        while curC != dc:
            print(mat[tr][curC])
            curC += 1
        while curR != dr:
            print(mat[curR][dc])
            curR += 1
        while curC != tc:
            print(mat[dr][curC])
            curC -= 1
        while curR != tr:
            print(mat[curR][tc])
            curR -= 1

m = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

mainD(m)














