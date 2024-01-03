from typing import List
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        ha = [2]
        va = [2]
        temp = -1
        for i in range(1,len(hBars)):
            if hBars[i] - hBars[i-1] == 1:
                ha[-1] += 1
            else:
                ha.append(2)
        for i in range(1,len(vBars)):
            if vBars[i] - vBars[i-1] == 1:
                va[-1] += 1
            else:
                va.append(2)
        # print(ha,va)
        ret = 1
        for x in ha:
            for y in va:
                z = min(x,y)
                ret = max(ret,z*z)
        return ret
