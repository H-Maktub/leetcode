from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        for i in range(1,len(prices)):
            t = prices[i]-prices[i-1]
            if t>0:
                ret+=t
        return ret