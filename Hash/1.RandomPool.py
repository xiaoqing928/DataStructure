'''
设计一种结构，在该结构中有如下三个功能：
insert(key)：将某个key加入到该结构，做到不重复加入。
delete(key)：将原本在结构中的某个key移除。 getRandom()：
等概率随机返回结构中的任何一个key。
[要求] Insert、delete和getRandom方法的时间复杂度都是
O(1)
'''
import random
'''
两个hash表，一个key+对应的index  一个index+对应的key 相当于反了反
删除的操作很酷炫，每次将最后一位的val赋给要删除的key所对应的val，然后将最后一位删除
'''
class RandomPool:
    hash1 = {}
    hash2 = {}
    def __init__(self):
        self.size = 3
    #直接加
    def insert(self, key, value):
        self.hash1[key] = value
        self.hash2[value] = key
    #要填洞，每次删除都把最后一位删掉，将其对应的值放入要删除的key所对应的值
    def delete(self, key, value):
        return 0
    #两个hash表，随机数返回
    def getRandom(self):
        index = int(random.random() * self.size)
        return self.hash2[index]

r = RandomPool()
r.insert('a', 0)
r.insert('b', 1)
r.insert('c', 2)
n0, n1, n2 = 0, 0, 0
for i in range(10000):
    val = r.getRandom()
    if val == 'a':
        n0 += 1
    elif val == 'b':
        n1 += 1
    else:
        n2 += 1
print(n0, n1, n2)