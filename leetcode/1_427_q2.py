from typing import List
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        ret = -1
        x = [[] for i in range(101)]
        y = [[] for i in range(101)]
        for p in points:
            x[p[0]].append(p[1])
            y[p[1]].append(p[0])
            x[p[0]].sort()
            y[p[1]].sort()
        def run(x1,y1):
            nonlocal ret
            ox1 = x1
            oy1 = y1
            for num in y[oy1]:
                if num > x1:
                    x1 = num
                    break
            for num in x[ox1]:
                if num > y1:
                    y1 = num
                    break
            if y1 in x[x1] and oy1 != y1  and x1 != ox1:
                area = (x1-ox1)*(y1-oy1)
                for i in range(ox1,x1+1):
                    c = 0
                    for j in x[i]:
                        if j == y1:
                            c+=1
                        if (j > oy1 and j < y1) or c > 1 :
                            area = -1
                for i in range(oy1,y1+1):
                    c = 0
                    for j in y[i]:
                        if j == x1:
                            c+=1
                        if (j > ox1 and j < x1) or c > 1 :
                            area = -1
                # print(ox1,oy1,x1,y1,y[oy1])
                ret = max(area,ret)
        for p in points:
            run(p[0],p[1])
        return ret
a = Solution()
b = a.maxRectangleArea([[33,92],[98,100],[33,100],[98,92],[42,100]])
print(b)