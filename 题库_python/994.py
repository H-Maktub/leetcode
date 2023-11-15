from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def zero(x,y):
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
                grid[x][y] = 2
        result = 0
        flag = True
        while flag:
            flag = False
            temp = []
            out = False
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if grid[x][y] == 2:
                        grid[x][y] = 0
                        temp.append([x,y])
                    elif grid[x][y] == 1:
                        out = True
            for t in temp:
                x = t[0]
                y = t[1]
                zero(x-1,y)
                zero(x+1,y)
                zero(x,y+1)
                zero(x,y-1)
            if len(temp) > 0 and out:
                result += 1
                flag = True
        for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if grid[x][y] == 1:
                        result = -1
        return result
a = Solution()
b = a.orangesRotting( [[2,1,1],[1,1,0],[0,1,1]])
print(b)