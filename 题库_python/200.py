from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def zero(x,y):
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == "1":
                grid[x][y] = "0"
                zero(x-1,y)
                zero(x+1,y)
                zero(x,y+1)
                zero(x,y-1)
                
            
        result = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    result += 1
                    zero(x,y)
                    print(x,y)
                    for z in grid:
                        print(z)
        return result
a = Solution()
b = a.numIslands([["1","0","1","1","1"],
                  ["1","0","1","0","1"],
                  ["1","1","1","0","1"]])
print(b)