from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        b = [[0]*(k+1) for _ in range(len(prices))]
        s = [[0]*(k+1) for _ in range(len(prices))]
        k = min(k,len(prices)//2)
        b[0][0]=-prices[0]
        for i in range(1, k + 1):
            b[0][i] = s[0][i] = float("-inf")

        for i in range(1,len(prices)):
            b[i][0] = max(b[i - 1][0], s[i - 1][0] - prices[i])
            for j in range(1,k+1):
                b[i][j] = max(b[i - 1][j], s[i - 1][j] - prices[i])
                s[i][j] = max(s[i - 1][j], b[i - 1][j - 1] + prices[i])
        return max(s[-1])

