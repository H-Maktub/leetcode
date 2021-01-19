from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        v1 = set()
        h1 = set()
        for i,temp in enumerate(matrix):
            for j,num in enumerate(temp):
                if num == 0:
                    v1.add(i)
                    h1.add(j)
        for i,temp in enumerate(matrix):
            for j,num in enumerate(temp):
                if i in v1 or j in h1:
                    matrix[i][j] = 0

if __name__ == "__main__":
    a = Solution()
    b=[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
    a.setZeroes(b)
    print(b)