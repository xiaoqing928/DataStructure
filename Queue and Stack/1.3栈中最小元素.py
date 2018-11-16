'''
实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
思路：两个栈，一个填数一个同步填最小值，同时弹出
'''
class Solution:
    def __init__(self):
        self.stack = []
        self.astack = []
    #2.stack正常压，astack比较栈顶元素
    def push(self, node):
        min = self.min()
        if node < min or not min:
            self.astack.append(node)
        else:
            self.astack.append(min)
        self.stack.append(node)
    #3.返回stack栈顶元素，astack也要出栈
    def pop(self):
        if self.stack:
            self.astack.pop()#stack的出栈 astack也要出栈
            return self.stack.pop()
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
    #4.栈顶即为最小
    def min(self):
        if self.astack:
            return self.astack[-1]
