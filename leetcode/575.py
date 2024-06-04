from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        m = len(set(candyType))
        return min(m,len(candyType)//2)
    

a = Solution()
b = a.distributeCandies([1,1,2,2,3,3])
print(b)