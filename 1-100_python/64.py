from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        temp = [[1] * m for i in range(n) ]
        for i in range(n):
            for j in range(m):
                if i ==0 and j==0:
                    temp[i][j] = grid[i][j]
                elif i ==0:
                    temp[i][j] = temp[i][j-1]+grid[i][j]
                elif j == 0:
                    temp[i][j] = temp[i-1][j]+grid[i][j]
                else:
                    temp[i][j] = min(temp[i][j-1],temp[i-1][j])+grid[i][j]
        return temp[-1][-1]

if __name__ == "__main__":
    a = Solution()
    b = a.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
    print(b)