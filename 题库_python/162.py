from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        for i in range(1,len(nums)):
            # print(i,i == len(nums)-1)
            if nums[i-1]<nums[i] and (i == len(nums)-1 or  nums[i]>nums[i+1]):
                return i
        return 0
    

a = Solution()
b = a.findPeakElement([1,2,3])
print(b)