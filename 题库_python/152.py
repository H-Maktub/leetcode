from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mmax = [-10] * len(nums)
        mmin = [-10] * len(nums)
        for i in range(len(nums)):
            mmax[i] = nums[i]
            mmin[i] = nums[i]
            if i > 0:
                mmax[i] = max(mmax[i], mmax[i-1]*nums[i], mmin[i-1]*nums[i])
                mmin[i] = min(mmin[i], mmax[i-1]*nums[i], mmin[i-1]*nums[i])
        print(mmax,mmin)
        return max(mmax)
a = Solution()
# b = a.maxProduct([2,3,-2,4])
# print(b)
b = a.maxProduct([-2,3,-4])
print(b)