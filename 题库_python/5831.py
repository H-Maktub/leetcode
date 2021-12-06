from typing import List
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort()
        print(milestones)
        t = 0
        while len(milestones) > 1:
            a = milestones.pop()
            b = milestones.pop()
            if a == b and len(milestones)>0 and a!=milestones[0]:
                t += (a-milestones[0])*2
                milestones.append(milestones[0])
                milestones.append(milestones[0])
                milestones.sort()
                print("==",t,milestones)
                continue
            t += min(a,b)*2
            c = abs(a-b)
            if c !=0:
                milestones.append(c)
                milestones.sort()
            print(t,milestones)
        t+=len(milestones)
        return t

a = Solution()
b = a.numberOfWeeks([1,2,3])
print("=================",b)
b = a.numberOfWeeks( [5,2,1])
print("=================",b)
b = a.numberOfWeeks([5,7,5,7,9,7])
print("=================",b)
b = a.numberOfWeeks([8,8,2,6])
print("=================",b)
