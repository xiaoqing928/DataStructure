'''
首先，要先判断两个链表是否相交,看两个链表尾部是否相同
其次，再找第一个相交点
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def searchFirstnode(node1, node2):
    count1, count2 = 0, 0
    cur1, cur2 = node1, node2
    while node1.next:
        node1 = node1.next
        count1 += 1
    while node2.next:
        node2 = node2.next
        count2 += 1
    if node1 != node2:
        return False
    if count1 >= count2:
        for i in range(count1-count2):
            cur1 = cur1.next
    else:
        for i in range(count2 - count1):
            cur2 = cur2.next
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1

a1 = Node(1)
a2 = Node(2)
a22 = Node(22)
a33 = Node(33)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a1.next = a2
a2.next = a3
a22.next = a33
a33.next = a4
a3.next = a4
a4.next = a5
r = searchFirstnode(a1, a22)
print(r.val)