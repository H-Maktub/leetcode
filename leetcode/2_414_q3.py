from typing import List
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        res = 0
        while i < n-1:
            j=i+1
            while j < n-1 and nums[j]<=nums[i]:
                j+=1
            res += (j-i)*nums[i]
            i = j
        return res
a = Solution()
b = a.findMaximumScore([1,3,1,5])
print(b)
b = a.findMaximumScore([4,3,1,3,2])
print(b)
