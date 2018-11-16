'''
给定一个链表的头节点head，请判断该链表是否为回
文结构。 例如： 1->2->1，返回true。 1->2->2->1，返回true。
15->6->15，返回true。 1->2->3，返回false。
'''
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
方法一：给一个额外的空间，遍历一遍放进栈，再遍历进行比较 n的额外空间
'''
a1 = Node(1)
a2 = Node(2)
a3 = Node(2)
a4 = Node(1)
a5 = Node(1)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

def servre(node):
    stack = []
    cur = node
    while node:
        v = node.val
        stack.append(v)
        node = node.next
    l = len(stack)-1
    while l>=0 and cur != None:
        if cur.val == stack.pop():
            cur = cur.next
            l -= 1
        else:
            return False
    return True
r = servre(a1)
print(r)
