from typing import List
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ii = len(grid)
        jj = len(grid[0])
        temp = [[0] * jj for _ in range(ii)]
        xp = [[0] * jj for _ in range(ii)]
        ret = 0
        def getNum(i,j)->int:
            num = 0
            if grid[i][j] == "X":
                num = 1
            elif grid[i][j] == "Y":
                num = -1 
            return num       
        for i in range(ii):
            for j in range(jj):
                num = getNum(i,j)
                xnum = max(num,0)
                if i == 0:
                    if j == 0:
                        temp[i][j] = num
                        xp[i][j] = xnum
                    else:
                        temp[i][j] = temp[i][j-1]+num
                        xp[i][j] = xp[i][j-1]+xnum
                else:
                    if j == 0:
                        temp[i][j] = temp[i-1][j]+num
                        xp[i][j] = xp[i-1][j]+xnum
                    else:
                        temp[i][j] = temp[i][j-1]+temp[i-1][j]-temp[i-1][j-1]+num
                        xp[i][j] = xp[i][j-1]+xp[i-1][j]-xp[i-1][j-1]+xnum
                if temp[i][j] == 0 and xp[i][j] > 0:
                    ret+=1
        return ret
    
a = Solution()
b = a.numberOfSubmatrices([["X","Y","."],["Y",".","."]])
print(b)

