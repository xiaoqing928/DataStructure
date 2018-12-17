'''
请把一段纸条竖着放在桌子上，然后从纸条的下边向
上方对折1次，压出折痕后展开。此时 折痕是凹下去的，即折痕
突起的方向指向纸条的背面。如果从纸条的下边向上方连续对折
2 次，压出折痕后展开，此时有三条折痕，从上到下依次是下折
痕、下折痕和上折痕。
给定一 个输入参数N，代表纸条都从下边向上方连续对折N次，
请从上到下打印所有折痕的方向。例如：N=1时，打印： down
N=2时，打印： down down up
'''
#思路：实质是中序遍历二叉树！！左子树全为down，右子树全为up！！
def printProcess(i, n, isdown):
    if n < i:
        return
    printProcess(i, n-1, True)
    if isdown:
        print('down')
    else:
        print('up')
    printProcess(i, n-1, False)
printProcess(1, 4, 1)