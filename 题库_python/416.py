from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l = len(nums)
        if l < 2:
            return False
        total = sum(nums)
        if total % 2 == 1:
            return False
        total = total//2
        if total < max(nums):
            return False
        dp = [[False] * (total+1) for _ in range(l)]
        for i in range(l):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1,l):
            num = nums[i]
            for j in range(1,total+1):
                if j >= num:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-num]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
        