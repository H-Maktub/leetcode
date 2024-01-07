from typing import List
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        t = 0
        for l in dimensions:
            new = l[0]*l[0] + l[1]*l[1]
            if new > t:
                t = new
                ans = l[0] * l[1]
            if new == t:
                ans = max(ans,l[0] * l[1])
        return ans
    
a = Solution()
b = a.areaOfMaxDiagonal( [[9,3],[8,6]])