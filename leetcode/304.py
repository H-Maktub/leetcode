from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.temp = [[0]*(m+1)]
        for i in range(n):
            self.temp.append([0])
            for j in range(m):
                self.temp[-1].append(matrix[i][j]+self.temp[i][j+1]+self.temp[i+1][j]-self.temp[i][j])
        for i in self.temp:
            print(i)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print(self.temp[row2+1][col2+1],self.temp[row1][col1],self.temp[row1][col2+1],self.temp[row2+1][col1])
        return self.temp[row2+1][col2+1]+self.temp[row1][col1]-self.temp[row1][col2+1]-self.temp[row2+1][col1]
if __name__ == "__main__":
    a = NumMatrix([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])
    print(a.sumRegion(2,1,4,3))