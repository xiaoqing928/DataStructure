'''
给定一个整型正方形矩阵matrix，请把该矩阵调整成
逆时针旋转90度的样子。
思路：还是先想一圈怎么搞，把问题简单化。
'''

m = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

class Solution:
    def mains(self,mat):
        tr, tc = 0, 0
        dr = len(mat) - 1
        dc = len(mat[0]) - 1
        return self.solution(mat, tr, tc, dr, dc)

    def solution(self, mat, tr, tc, dr, dc):
        c = 0 #计数
        while c < dc-tc:
            temp = mat[tr][tc+c]
            mat[tr][tc+c] = mat[tr+c][dc]
            mat[tr+c][dc] = mat[dr][dc-c]
            mat[dr][dc-c] = mat[dr-c][tc]
            mat[dr-c][tc] = temp
            c += 1
        while tr != dr-1:
            tr += 1
            tc += 1
            dr -= 1
            dc -= 1
            self.solution(mat, tr, tc, dr, dc)
        return mat

# def solution(mat, tr, tc, dr, dc):
#     c = 0 #计数
#     while c < dc-tc:
#         temp = mat[tr][tc+c]
#         mat[tr][tc+c] = mat[tr+c][dc]
#         mat[tr+c][dc] = mat[dr][dc-c]
#         mat[dr][dc-c] = mat[dr-c][tc]
#         mat[dr-c][tc] = temp
#         c += 1
#     while tr != dr-1:
#         tr += 1
#         tc += 1
#         dr -= 1
#         dc -= 1
#         solution(mat, tr, tc, dr, dc)
#     return mat
# r = solution(m, 0, 0, 3, 3)
# print(r)

a = Solution()
r = a.mains(m)
print(r)