from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        t = [0]*n
        for i in range(n):
            t[i] = nums[nums[i]]
        return t