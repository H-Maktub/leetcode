from typing import List, Text, TextIO
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        for i in  range(m):
            grid2[i].append(0)
        grid2.append([0]*n)
        ret = 0
        temp = [[0]*n for _ in range(m)]
        def getTree(i,j)->bool:
            nonlocal temp
            if -1<i<m and -1<j<n and grid2[i][j] == 1 :
                if temp[i][j] == 0:
                    temp[i][j] = 1
                    a = getTree(i+1,j)
                    b = getTree(i,j+1)
                    c = getTree(i-1,j)
                    d = getTree(i,j-1)
                    if grid1[i][j] != 1 or a == False or b == False or c == False or d == False:
                        return False
            return True

        for i in range(m):
            for j in range(n):
                if temp[i][j] == 0 and grid2[i][j]==1:
                    if  getTree(i,j) == True:
                        ret+=1
        return ret

a = Solution()
# b = a.countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])
# print(b)
# b = a.countSubIslands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]])
# print(b)
b = a.countSubIslands([
    [1,1,0,1,0,1,1,1],
    [0,1,1,1,1,0,1,1],
    [1,1,1,1,0,1,0,1],
    [1,1,1,0,1,1,1,1],
    [1,1,1,1,0,1,1,0],
    [1,1,1,1,0,1,0,0],
    [1,0,1,1,1,1,0,0],
    [1,0,0,1,1,1,1,1]
    ], 
    [
        [1,1,1,1,0,0,0,0],
        [0,1,1,1,0,0,1,1],
        [1,1,1,1,0,1,1,1],
        [1,1,0,1,1,1,1,0],
        [1,0,0,1,0,1,1,1],
        [1,1,0,1,1,1,1,0],
        [1,0,1,0,1,1,1,1],
        [1,1,1,1,1,0,1,1]])
print(b)
