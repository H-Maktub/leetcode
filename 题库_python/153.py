from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            t = left+(right-left)//2
            if nums[t] < nums[right]:
                right = t
            else:
                left = t+1
        return nums[left]