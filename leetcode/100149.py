from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        t = set()
        ret = [0,0]
        for i in grid:
            for j in i:
                if j not in t:
                    t.add(j)
                else:
                    ret[0] = j
        
        for i in range(1,len(grid)*len(grid)+1):
            if i not in t:
                ret[1] = i
        return ret