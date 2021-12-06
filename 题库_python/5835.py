from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m = float('inf')
        n = 1
        r = 0
        for t in matrix:
            for i in t:
                if i<0:
                    n=-n
                r+=abs(i)
                m = min(m,abs(i))
        print(r,)
        if n<=0:
            r = r-2*m 
        return r

a = Solution()
b = a.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]])
print(b)