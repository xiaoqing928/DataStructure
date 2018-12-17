'''
中序遍历的整体顺序为 左-中-右
可以这样想，（1）如果一个节点有右子树，那么这个节点的后继节点为 右子树中的最左节点（左中右是一个整体，有右之后还是先输出右子树整体的最左节点）
          （2）如果一个节点没有右子树，则往上寻找，当父节点的左孩子等于当前节点时，父节点即为当前节点的后序节点
'''
class Node:
    left = None
    right = None
    parent = None
    def __init__(self, val):
        self.val = val

def getLeftMost(node):
    '''
    :param node:节点
    :return: 该头节点形成的树中的最左节点
    '''
    while node.left:
        node = node.left
    return node

def getSuccessorNode(node):
    if node == None:
        return node
    #如果一个节点有右子树，该节点的后继节点则为右子树的最左节点
    if node.right != None:
        return getLeftMost(node.right)#找到某棵树的最左节点
    else:
        parent = node.parent
        #如果该节点为其父节点的左孩子，则返回父节点。（从整体左-中-右的大框架上去理解）
        while parent != None and parent.left != node:#
            node = parent
            parent = node.parent
        return parent

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)
a7 = Node(7)
a1.left, a1.right = a2, a3
a2.left, a2.right = a4, a5
a3.left, a3.right = a6, a7
a4.parent = a2
a5.parent = a2
a2.parent = a1
a6.parent, a7.parent = a3, a3
a3.parent = a1
r = getSuccessorNode(a7)
print(r)




