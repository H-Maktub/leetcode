from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        temp = [[1] * m for i in range(n) ]
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    temp[i][j] = 0
                elif i ==0:
                    temp[i][j] = temp[i][j-1]
                elif j == 0:
                    temp[i][j] = temp[i-1][j]
                else:
                    temp[i][j] = temp[i][j-1]+temp[i-1][j]
        return temp[-1][-1]

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
