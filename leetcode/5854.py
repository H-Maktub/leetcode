from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        t = []
        for i in range(k-1,len(nums)):
            t.append(nums[i]-nums[i-k+1])
        return min(t)

a = Solution()
b = a.minimumDifference([9,4,1,7],2)
print(b)