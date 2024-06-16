from typing import List
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        ret = nums[0]
        dp = [float('-inf'),float('-inf')]
        dp[nums[0] % 2] = nums[0]
        for i in range(1,len(nums)):
            p = nums[i] % 2
            cur = max(dp[p]+nums[i],dp[1-p]-x+nums[i])
            ret = max(ret,cur)
            dp[p] = max(dp[p],cur)  
        return ret
    

a = Solution()
b = a.maxScore([2,3,6,1,9,2],5)
print(b)