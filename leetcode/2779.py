from typing import List
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ret=l=0
        n = len(nums)
        nums.sort()
        for i in range(n):
            while nums[i] - 2*k > nums[l]:
                l+=1
            ret = max(ret,i-l+1)
        return ret
a = Solution()
b = a.maximumBeauty([4,6,1,2],2)
print(b)

b = a.maximumBeauty([49,26],12)
print(b)