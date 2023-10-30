from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = 0
        y = len(matrix[0])-1
        while x < len(matrix) and y>=0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1

        return False
    
a = Solution()
b = a.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5)
print(b)
b = a.searchMatrix([[-5]],-5)
print(b)
b = a.searchMatrix([[1,4],[2,5]],2)
print(b)
b = a.searchMatrix([[-1,3]],1)
print(b)