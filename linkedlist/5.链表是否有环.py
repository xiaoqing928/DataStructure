'''
1.用hashset把节点都放进去，有相同的对象则说明存在环
2.用之前自己的老方法，准备两个指针，一个快指针，一个慢指针，
相遇之后快指针回 头节点且一次走一步，最终位置即为入口点（数学归纳法）4-2.26
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

'''
一、双指针
'''
def isloop(node):
    if node == None or node.next == None:
        return None
    less, quick, cur = node, node, node
    less = less.next
    quick = quick.next.next
    while less != quick and quick.next.next:
        less = less.next
        quick = quick.next.next
    if less != quick:
        return False
    else:
        while cur != less:
            less = less.next
            cur = cur.next
        return cur

'''
hash结构，将节点对象作为key
'''
def isloop2(node):
    dict = {}
    while node:
        if node in dict:
            return node
        else:
            dict[node] = node.val
        node = node.next
a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a3
r = isloop2(a1)
print(r.val)
























