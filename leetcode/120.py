from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        temp = [[0] * n for _ in range(n)]
        temp[0][0] = triangle[0][0]
        for i in range(1,n):
            temp[i][0] = temp[i-1][0]+triangle[i][0]
            for j in range(1,i):
                temp[i][j] = min(temp[i-1][j-1],temp[i-1][j])+triangle[i][j]
            temp[i][i] = temp[i-1][i-1] + triangle[i][i]
        print(temp[-1])
        return min(temp[-1])

a = Solution()
b = a.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(b)
