from typing import List
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                x,y = nums[i],nums[j]
                if abs(x-y)<=min(x,y):
                    result = max(result,x^y)
        return result
