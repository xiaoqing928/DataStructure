#给定一个数组，求如果排序之后，相邻两数的最大差值，要求时
#间复杂度O(N)，且要求不能用非基于比较的排序

class MaxGap:
    def maxGap(self, arr):
        l = len(arr)
        # 空或只有一个数直接返回0
        if l < 2:
            return 0
        m, n = max(arr), min(arr)  # 最大最小值
        if m == n:
            return 0
        buckets = l + 1  # 桶的数量
        # parts = int((m-n) / l) #区间间隔
        boollist = [[]] * buckets  # 记录是否为空
        maxlist = [[]] * buckets  # 记录最大值
        minlist = [[]] * buckets  # 记录最小值

        # 放到哪个桶里
        for i in range(l):
            r = self.whereBuckets(arr[i], n, m, l)
            boollist[r] = arr[i]
            if maxlist[r] == []:
                maxlist[r] = arr[i]
            elif boollist[r] != [] and maxlist[r] < arr[i]:
                maxlist[r] = arr[i]
            if minlist[r] == []:
                minlist[r] = arr[i]
            elif boollist[r] != [] and minlist[r] > arr[i]:
                minlist[r] = arr[i]
        res = 0
        lastmax = maxlist[0]
        for i in range(1, buckets):
            if boollist[i] != []:
                minb = minlist[i]
                res = max(minb - lastmax, res)
                lastmax = minlist[i]
        return res
    def whereBuckets(self, num, min, max, len):
        return int((num - min) / (max - min) * len)

a = MaxGap()
r = a.maxGap([1,100,1000000])
print(r)