'''
用一个固定数组创建一个队列
思路：start和end两个指针，start返回值，end加入值，同时判断和数组size的大小
相当于start和end在转圈
'''

class Queue:
    start, end = 0, 0
    arr = [[]]
    size = 0
    def __init__(self, l):
        self.arr = self.arr * l
    def push(self, num):
        if self.size < len(self.arr):
            self.arr[self.end % len(self.arr)] = num
            self.end += 1
            self.size += 1
        else:
            print('arr is full')
    def poll(self):
        if self.size > 0:
            self.size -= 1
            self.start += 1
            return self.arr[(self.start-1) % len(self.arr)]
        else:
            print('arr is null')

a = Queue(2)
a.push(1)
a.push(2)
print(a.arr)
a.push(3)
print(a.poll())
a.push(3)
a.push(3)
print(a.poll())