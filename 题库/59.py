from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        retList = [[0 for _ in range(n)] for _ in range(n)]
        nums = 1
        i = 0  
        while nums <= n*n:
            if i == n-1-i:
                retList[i][i] = nums
                break
            for x in range(i,n-1-i):
                retList[i][x] = nums
                nums +=1
            for x in range(i,n-1-i):
                retList[x][n-1-i] = nums
                nums +=1
            for x in range(i,n-1-i):
                retList[n-1-i][n-1-x] = nums
                nums +=1
            for x in range(i,n-1-i):
                retList[n-1-x][i] = nums
                nums +=1
            i+=1
        return retList

if __name__ == "__main__":
    a = Solution()
    b = a.generateMatrix(3)
    print(b)