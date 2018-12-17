'''
准备一个栈 往里压数据
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

def preOrderUnRecur(node):
    stack = []
    if node != None:
        stack.append(node)
        while stack:
            node = stack.pop()
            print(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)

def inOrderUnRecur(node):
    stack = []
    if node != None:
        while stack or node:
            if node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.val)
                node = node.right

def posOrderUnRecur(node):
    stack1 = []
    stack2 = []
    if node != None:
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left != None:
                stack1.append(node.left)
            if node.right != None:
                stack1.append(node.right)
    while stack2:
        print(stack2.pop().val)
# preOrderUnRecur(tree1)
inOrderUnRecur(tree1)
# posOrderUnRecur(tree1)