from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(m, n):
            return m if not n else gcd(n, m%n)
        
        def getslope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            
            if dx == 0: return (p1[0], 0)
            if dy == 0: return (0, p1[1])
            
            d = gcd(dx, dy)
            return (dx//d, dy//d)
        
        ret = 0
        for i in range(len(points)):
            temp = {}
            r = 0
            for j in range(i+1,len(points)):
                key = getslope(points[i],points[j])
                if key in temp:
                    temp[key] += 1
                else:
                    temp[key] = 1
                r = max(r,temp[key])
            ret=max(r+1,ret)
        return ret
                

