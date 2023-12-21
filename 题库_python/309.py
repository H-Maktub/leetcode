from functools import cache
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i,hold)->float:
            if i<0:
                return float('-inf') if hold else 0
            if hold:
                return max(dfs(i-1,True),dfs(i-2,False)-prices[i])
            return max(dfs(i-i,False),dfs(i-1,True)+prices[i])
        return dfs(n-1,False)