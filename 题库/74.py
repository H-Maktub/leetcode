from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ret = False
        n = len(matrix[0])
        for temp in matrix:
            if target <=temp[n-1]:
                for num in temp:
                    if target == num:
                        return True
                    elif target<num:
                        break
        return ret

if __name__ == "__main__":
    a = Solution()
    b = a.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)
    print(b)