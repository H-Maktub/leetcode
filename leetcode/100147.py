from typing import List
import collections
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ret = 0
        temp = {}
        dp = collections.deque()
        for n in nums:
            if n not in temp:
                temp[n] = 0
            if temp[n] < k:
                dp.append(n)
                temp[n]+=1
            else:
                while len(dp) > 0:
                    m = dp.popleft()
                    temp[m]-=1
                    if m == n:
                        dp.append(n)
                        temp[n]+=1
                        break

            ret = max(ret,len(dp))
        return ret
    

a = Solution()
b = a.maxSubarrayLength([2,1,1,3],1)
print(b)