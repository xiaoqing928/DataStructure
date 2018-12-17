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

def pro(node):
    if node == None:
        return True, 0
    l = pro(node.left)
    if l[0] is False:
        return False
    r = pro(node.right)
    if r[0] is False:
        return False
    if abs(l[1]-r[1]) > 1:
        return False
    return True, max(l[1],r[1])+1

class returnData:
    def __init__(self, isB, level):
        self.isB = isB
        self.level = level

def recurProcess(node):
    if node == None:
        return returnData(True, 0)
    l = recurProcess(node.left)
    if l.isB == False:
        return returnData(False, 0)
    r = recurProcess(node.right)
    if r.isB == False:
        return returnData(False, 0)
    if abs(l.level-r.level) > 1:
        return returnData(False, 0)
    return returnData(True, max(l.level, r.level) + 1)

def isBalance(node):
    return recurProcess(node).isB

r = isBalance(tree1)
print(r)