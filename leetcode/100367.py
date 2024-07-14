from typing import List
from functools import cache
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # cuts = [(cost, 'H') for cost in horizontalCut] + [(cost, 'V') for cost in verticalCut]
        # print(cuts)
        ret = 0
        horizontalCut.sort()
        verticalCut.sort()
        h = 1
        v = 1
        while len(horizontalCut) + len(verticalCut) > 0:
            r1 = 0
            if len(horizontalCut) > 0:
                r1 = horizontalCut[-1]
            r2 = 0
            if len(verticalCut) > 0:
                r2 = verticalCut[-1]
            if r1 > r2:
                h+=1
                ret+=horizontalCut.pop()*v
            else:
                v+=1
                ret+=verticalCut.pop()*h
        return ret
    

a = Solution()
b = a.minimumCost(3,2,[1,3],[5])
print(b)
b = a.minimumCost(2,2,[7],[4])
print(b)
b = a.minimumCost(7,4,[13,6,12,14,4,7],[14,15,11])
print(b)

# m =
# 7
# n =
# 4
# horizontalCut =
# [13,6,12,14,4,7]
# verticalCut =
# [14,15,11]
# 258