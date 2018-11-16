
def whereBuckets(num, min, max, len):
    return int(num-min/(max-min)*len)

r = whereBuckets(8,1,8,6)
print(r)

print(max(1,2))




import numpy as np

arr = np.array(['米饭','刀削面','拉条子','泡馍','黄焖鸡','水饺','麻辣烫','米粉','砂锅','屎'])
# print('今天中午吃啥:',np.random.choice(arr))
a = [[]]*3
a[2]=1
print(a)
print(a[2] == [])