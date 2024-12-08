from typing import List
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = -1
        for i in range(len(nums)-l+1):
            for j in range(i+l-1,min(i+r,len(nums))):
                print(nums[i:j+1])
                su = sum(nums[i:j+1])
                if su > 0:
                    if res == -1:
                        res = su
                    else:
                        res = min(res,su)
        return res
# a = Solution()
# b = a.minimumSumSubarray([3, -2, 1, 4],2,3)
a = Solution()
b = a.minimumSumSubarray([7,3],2,2)

