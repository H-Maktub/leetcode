from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []
        for i in range(len(nums)):
            result.append(1)
            for j in range(i):
                if nums[i]>nums[j]:
                    result[i] = max(result[i],result[j]+1)
        return max(result)