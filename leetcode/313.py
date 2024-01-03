from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        p = [1]*len(primes)
        nums = primes[:]
        for i in range(2,n+1):
            print(dp,p,nums)
            m = min(nums)
            dp[i] = m
            for j in range(len(primes)):
                if nums[j] == m:
                    p[j]+=1
                    nums[j] = dp[p[j]]*primes[j]
        return dp[-1]
    

a = Solution()
b = a.nthSuperUglyNumber(12,[2,7,13,19])