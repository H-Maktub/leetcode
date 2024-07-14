from typing import List
class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        m = min(enemyEnergies)
        if m > currentEnergy:
            return 0
        currentEnergy += sum(enemyEnergies)-m
        return currentEnergy // m


a = Solution()
b = a.maximumPoints([3,2,2],2)
print(b)
b = a.maximumPoints([2],10)
print(b)
                    
