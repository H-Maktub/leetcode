from typing import List
from math import comb
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        if obstacleGrid[0][0] == 1 or obstacleGrid[n-1][m-1]==1:
            return 0
        max =comb(m + n - 2, m - 1)
        print(max,m,n)
        for i in range(0,n):
            for j in range(0,m):
                if obstacleGrid[i][j] == 1:
                    a = comb(m + n - 2-i-j, m - 1-j)
                    if j!=0 and i!=n-1:
                        print('a',i,j,a)
                        max -=a
                    if i!=0 and j!=m-1:
                        print('b',i,j,a)
                        max -=a
        return max

if __name__ == "__main__":
    a = Solution()
    b = a.uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
    print('=====',b)
    b = a.uniquePathsWithObstacles([[0,1],[0,0]])
    print('=====',b)
    b = a.uniquePathsWithObstacles([
        [0,0,0,0],
        [0,1,0,0],
        [0,0,0,0],
        [0,0,1,0],
        [0,0,0,0]])
    print('=====',b)
