from typing import List,Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums = Counter(nums).values()
        nums = Counter(nums)
        return max(nums) * nums[max(nums)]
    
a = Solution()
b = a.maxFrequencyElements([1,2,2,3,1,4])
print(b)
b = a.maxFrequencyElements([1,2,3,4,5])
print(b)