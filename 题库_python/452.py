from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p:p[1])
        print(points)
        ret = 1
        r = points[0][1]
        for p in points:
            if p[0] > r:
                r = p[1]
                ret += 1
        return ret

a = Solution()
b = a.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])