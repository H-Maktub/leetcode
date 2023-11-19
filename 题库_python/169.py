from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        temp = {}
        for num in nums:
            if num not in temp:
                temp[num] = 0
            temp[num] += 1
            if temp[num] >= n:
                return num
        return -1