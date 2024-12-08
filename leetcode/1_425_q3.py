from typing import List
import math
class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        def dfs(i,p1,p2)->int:
            if i>=len(nums):
                return 0
            res = nums[i]+dfs(i+1,p1,p2)
            if p1 < op1 and p2 < op2 and nums[i]>=k:
                t1 = math.ceil(nums[i]/2)-k
                t2 = math.ceil((nums[i]-k)/2)
                if t1 > 0:
                    t2 = min(t2,t1)
                res = min(res, t2 + dfs(i+1,p1+1,p2+1))
            if p1 < op1:
                res = min(res,math.ceil(nums[i]/2) + dfs(i+1,p1+1,p2))
            if p2 < op2 and nums[i]>=k:
                res = min(res,nums[i]-k + dfs(i+1,p1,p2+1))
            return res
        return dfs(0,0,0)
a = Solution()
b = a.minArraySum( [2,8,3,19,3],3,1,1)
print(b)
b = a.minArraySum([2,4,3],3,2,1)
print(b)
b = a.minArraySum([10],3,1,1)
print(b)