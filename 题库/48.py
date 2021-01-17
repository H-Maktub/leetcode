from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        new = [[0] *n for num in range(n)]
        
        for i in range(n):
            for j in range(n):
                new[j][n-1-i] = matrix[i][j]
        matrix[:] = new
        print(new)



if __name__ == "__main__":
    a = Solution()
    b = a.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])
    pass