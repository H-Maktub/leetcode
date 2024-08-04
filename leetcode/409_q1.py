from typing import List
class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.temp = grid
        self.n = len(self.temp)

    def adjacentSum(self, value: int) -> int:
        for i in range(self.n):
            for j in range(self.n):
                if self.temp[i][j] == value:
                    res = 0
                    if i - 1 >= 0:
                        res+=self.temp[i-1][j]
                    if j - 1 >= 0:
                        res+=self.temp[i][j-1]
                    if i + 1 < self.n:
                        res+=self.temp[i+1][j]
                    if j + 1 < self.n:
                        res+=self.temp[i][j+1]
                    return res

    def diagonalSum(self, value: int) -> int:
        for i in range(self.n):
            for j in range(self.n):
                if self.temp[i][j] == value:
                    res = 0
                    if i - 1 >= 0 and j - 1 >= 0:
                        res+=self.temp[i-1][j-1]
                    if i - 1 >= 0 and j + 1 < self.n:
                        res+=self.temp[i-1][j+1]
                    if i + 1 < self.n and j - 1 >= 0:
                        res+=self.temp[i+1][j-1]
                    if j + 1 < self.n and i + 1 < self.n:
                        res+=self.temp[i+1][j+1]
                    return res



Your neighborSum object will be instantiated and called as such:
obj = neighborSum(grid)
param_1 = obj.adjacentSum(value)
param_2 = obj.diagonalSum(value)