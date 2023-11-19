from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(num)->int:
            if num < 0: return -1
            if num == 0: return 0
            m = int(1e9)
            for coin in coins:
                res = dp(num  - coin)
                if res >= 0 and res<m:
                    m = res+1
            return m if m < int(1e9) else -1
        if amount < 1:
            return 0
        return dp(amount)