from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        ret = 0
        temp = nums[0]
        while l<=r and r < len(nums):               
            if temp >= target:
                if ret == 0:
                    ret = r-l+1
                ret = min(ret,r-l+1)
                if l == r:
                    r+=1
                    if r < len(nums):
                        temp+=nums[r]
                else:
                    temp-=nums[l]
                    l+=1
            else:
                r+=1
                if r < len(nums):
                    temp+=nums[r]
        return ret
            
a = Solution()
b = a.minSubArrayLen(7,[2,3,1,2,4,3])