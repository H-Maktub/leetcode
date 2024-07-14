from typing import List
from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def count(i,t)->int:
            if i == n-1:
                if t == target:
                    return 1
                else:
                    return 0
            return count(i+1,t+nums[i+1])+count(i+1,t-nums[i+1])
        return count(0,nums[0])+count(0,-nums[0])
    

a = Solution()
b = a.findTargetSumWays([1,1,1,1,1],3)
print(b)
b = a.findTargetSumWays([10,34,28,5,10,26,9,17,28,10,9,6,10,15,0,28,42,39,25,19],26)
print(b)