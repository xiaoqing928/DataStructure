'''
用数组结构实现大小固定栈
思路：有一个指针index指向数组开始的位置，加入一个数，判断index和数组size的大小，指针下移
只需要管index即可
'''

class stack:
    index = 0  # 当前指向的位置
    arr = [[]]
    def __init__(self, n):
        self.arr = self.arr * n

    def push(self, num):
        if self.index < len(self.arr):
            self.arr[self.index] = num
            self.index += 1
        else:
            print('arr is full!')
    def peek(self):
        if self.index == 0:
            return None
        return self.arr[self.index-1]
    def pop(self):
        if self.index == 0:
            return None
        r = self.arr[self.index-1]
        self.index -= 1
        return r
a = stack(3)
print(a.arr)
a.push(1)
a.push(2)
a.push(3)
print(a.arr)
print(a.peek())
a.push(4)
print(a.pop())
a.push(4)
print(a.arr)