from typing import List
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        a = 0
        for i in range(m):
            for j in range(n//2):
                if grid[i][j] != grid[i][n-1-j]:
                    a+=1
        b = 0
        for j in range(n):
            for i in range(m//2):
                if grid[i][j] != grid[m-1-i][j]:
                    b+=1
        print(a,b)
        return min(a,b)
    

a = Solution()
b = a.minFlips([[1,0,0],[0,0,0],[0,0,1]])
print(b)
b = a.minFlips([[1,0,0],[0,0,0],[0,0,1]])
print(b)