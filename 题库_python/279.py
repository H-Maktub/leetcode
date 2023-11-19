from math import sqrt
import sys
class Solution:
    def numSquares(self, n: int) -> int:
        result = [0] * (n+1)
        for i in range(1,n+1):
            m = 100000
            j = 1
            while j*j<=i:
                m = min(m,result[i-j*j])
                j+=1
            result[i] = m+1
            print(result)
        return result[n] 
        
a = Solution()
b = a.numSquares(12)