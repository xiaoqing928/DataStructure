'''
方法二：
一个快指针一个慢指针
慢指针之后的入栈，慢指针几乎到中点的位置
coding自己掌握
n/2的额外空间
'''

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
# a5 = Node(1)
a1.next = a2
a2.next = a3
a3.next = a4
# a4.next = a5

def reserver1(node):
    if node == Node or node.next == Node:
        return True
    slow, quick, cur = node, node, node
    while quick.next and quick.next.next:
        slow = slow.next
        quick = quick.next.next
    stack = []
    mid = slow
    n = slow.next
    while n:
        stack.append(n.val)
        n = n.next
    while stack:
        if cur.val != stack.pop():
            return False
        cur = cur.next
    return True
# r = reserver1(a1)
# print(r)

while a1.next:
    print(a1.next)
    a1 = a1.next









