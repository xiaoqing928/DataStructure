class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solusion:
    def printPartition(self, node1, node2):
        while node1 and node2:
            if node1.value == node2.value:
                print(node1.value)
                node1 = node1.next
                node2 = node2.next
            else:
                break

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
b1 = Node(1)
b2 = Node(2)
b3 = Node(3)
b4 = Node(3)
a1.next = a2
a2.next = a3
b1.next = b2
b2.next = b3
b3.next = b4
r = Solusion()
r.printPartition(a1, b1)



