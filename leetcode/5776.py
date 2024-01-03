from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        temp = [True,True,True,True]
        for i in range(n):
            for j in  range(n):
                if temp[0] and mat[i][j] != target[i][j]:
                    temp[0] = False
                if temp[1] and mat[i][j] != target[j][n-1-i]:
                    temp[1] = False
                if temp[2] and mat[i][j] != target[n-1-i][n-1-j]:
                    temp[2] = False
                if temp[3] and mat[i][j] != target[n-1-j][i]:
                    temp[3] = False
        return max(temp)
a = Solution()
b = a.findRotation([[0,0,0],[0,1,0],[1,1,1]],[[1,1,1],[0,1,0],[0,0,0]])
print(b)