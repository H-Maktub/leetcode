from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = max(prices)
        ret = 0
        for p in prices:
            ret = max(ret,p-m)
            m = min(m,p)
        return ret

a = Solution()
b = a.maxProfit([7,1,5,3,6,4])
print(b)
