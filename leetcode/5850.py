from typing import List
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(nums[0],-1,-1):
            if nums[-1]%i==0 and nums[0]%i==0:
                return i
        return 1