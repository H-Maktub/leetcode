from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        result = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[i] = nums[i]
            elif i == 1:
                result[i] = max(nums[0],nums[1])
            else:
                result[i] = max(result[i-2]+nums[i],result[i-1])
        return result[-1]