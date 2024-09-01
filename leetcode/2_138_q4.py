from typing import List
import functools
import math
class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        temp = [[damage[i]/math.ceil(health[i]/power),math.ceil(health[i]/power),i] for i in range(len(damage))]
        total = sum(damage)
        temp.sort(reverse=True)
        # print(temp)
        res = 0
        for i in range(len(damage)):
            res+=total*temp[i][1]
            total-=damage[temp[i][2]]
        return res

a = Solution()
b = a.minDamage(4,[1,2,3,4],[4,5,6,8])
print(b)
b = a.minDamage(1,[1,1,1,1],[1,2,3,4])
print(b)
b = a.minDamage(8,[40],[59])
print(b)
b = a.minDamage(62,[80,79],[86,13])
print(b)