
from typing import ByteString, List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in matrix:
            print(i)
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        temp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    temp[i][j+1] = temp[i][j]+1
                else:
                    temp[i][j+1] = 0
        for i in temp:
            print(i)
        ret = 0
        for i in range(n+1):
            s = [-1]
            for j in range(m+1):
                num = temp[j][i]
                while temp[s[-1]][i]> num:
                    print("ding",temp[s[-1]][i],num)
                    h = temp[s.pop()][i]
                    w = j-s[-1]-1
                    ret = max(ret,h*w)
                s.append(j)
        return ret



if __name__ == "__main__":
    a = Solution()
    b = a.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
    print("============",b)
    b = a.maximalRectangle([["0","0","0","0","0","0","1"],["0","0","0","0","1","1","1"],["1","1","1","1","1","1","1"],["0","0","0","1","1","1","1"]])
    print("============",b)
    b = a.maximalRectangle([["0","0","1"],["1","1","1"]])
    print("============",b)
    