'''
平衡二叉树：左右子树高度差不大于1
'''

class Tree:
    left = None
    right = None
    def __init__(self, val):
        self.val = val

tree1 = Tree(1)
tree2 = Tree(2)
tree3 = Tree(3)
tree4 = Tree(4)
tree5 = Tree(5)
tree1.left = tree2
tree1.right = tree3
tree2.left = tree4
tree2.right = tree5

class returnData():
    def __init__(self, isB, level):
        self.isB = isB
        self.level = level

def recurProcess(node):
    if node == None:
        return returnData(True, 0)
    leftData = recurProcess(node.left)
    if leftData.isB is False:
        return returnData(False, 0)
    rightData = recurProcess(node.right)
    if rightData.isB is False:
        return returnData(False, 0)
    if abs(leftData.level-rightData.level) > 1:
        return returnData(False, 0)
    return returnData(True, max(leftData.level, rightData.level) + 1)

def isBalance(node):
    return recurProcess(node).isB

r = recurProcess(tree1).isB
print(r)
















