from typing import List
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        temp = set()
        for p in points:
            if p[0] not in temp:
                temp.add(p[0])
        li = list(temp)
        li.sort()   
        if w == 0:
            return len(li)
        pre = None
        ret = 0
        for n in li:
            if pre == None or n - pre > w:
                pre = n
                ret+=1
        return ret

a = Solution()
b = a.minRectanglesToCoverPoints([[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]],1)
print(b)
b = a.minRectanglesToCoverPoints([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]],2)
print(b)
b = a.minRectanglesToCoverPoints([[2,3],[1,2]],0)
print(b)