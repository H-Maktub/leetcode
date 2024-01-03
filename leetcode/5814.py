from typing import List
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        rungs.insert(0,0)
        ret = 0
        for i in range(1,len(rungs)):
            run = rungs[i]-rungs[i-1]
            if run > dist:
                t = run//dist-1
                if run%dist != 0:
                    t+=1
                ret+=t
        return ret

a = Solution()
b = a.addRungs([1,3,5,10],2)
print("====================",b)
