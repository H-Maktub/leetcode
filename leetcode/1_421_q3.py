from functools import cache
from typing import List
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        res = 0
        a = ord('a')
        z = ord('z')+1-a
        @cache
        def getLength(c,n)->int:
            nonlocal nums
            if n == 0:
                return 1
            ret = 0
            for i in range(nums[c]):
                ret+=getLength((c+1+i)%26,n-1)
            return ret%1000000007
        for ch in s:
            res=(res+getLength(ord(ch)-a,t))%1000000007
        return res
    
a = Solution()
b = a.lengthAfterTransformations("u",5,[1,1,2,2,3,1,2,2,1,2,3,1,2,2,2,2,3,3,3,2,3,2,3,2,2,3])
print(b)