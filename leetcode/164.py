from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0
        for i in range(1,len(nums)):
            ret = max(ret, nums[i] - nums[i-1])
        return ret