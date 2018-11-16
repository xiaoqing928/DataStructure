'''
时间复杂度O（NlogN） 额外空间复杂度O（N）
'''
arr = [4,3,2,1,15,17,19,11111,456,67,656,362,2,343,645,3,536,6,46,45,64,7,78,9,8979,52,2323]

def merge(arr, l, r, mid):
    help = []
    p1 = l
    p2 = mid+1
    while p1<=mid and p2 <= r:
        if arr[p1] < arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1
    if p1 <= mid:
        for i in range(p1,mid+1):
            help.append(arr[i])
    if p2 <= r:
        for i in range(p2, r + 1):
            help.append(arr[i])
    le = len(help)
    for i in range(le):
        arr[l+i] = help[i]

def sortP(arr, l, r):
    if l == r:
        return
    mid = int((l + r) / 2)
    # mid = (l + r) >> 1
    sortP(arr, l, mid)
    sortP(arr, mid+1, r)
    merge(arr, l, r, mid)

sortP(arr, 0, len(arr)-1)
print(arr)
# arr.sort()
# print(arr)