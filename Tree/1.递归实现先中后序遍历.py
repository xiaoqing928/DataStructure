'''
按照递归访问节点的顺序，打印第一次出现的就是先序，打印中间的就是中序，打印最后出现的就是后序
14.00解析  一个节点访问三次
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
# print(tree1.left.right.val)

#先序
def preOrderRecur(node):
    if node == None:
        return
    print(node.val, end='->')
    preOrderRecur(node.left)
    preOrderRecur(node.right)

#中序
def inOrderRecur(node):
    if node == None:
        return
    inOrderRecur(node.left)
    print(node.val, end='->')
    inOrderRecur(node.right)

#后序
def posOrderRecur(node):
    if node == None:
        return
    posOrderRecur(node.left)
    posOrderRecur(node.right)
    print(node.val, end='->')

preOrderRecur(tree1)
print('None')
inOrderRecur(tree1)
print('None')
posOrderRecur(tree1)
print('None')