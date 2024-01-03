from typing import List, SupportsAbs
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        t = list(num)
        tag = True
        for i in range(len(num)):
            tt  = int(num[i])
            if tt < change[tt]:
                t[i] = str(change[tt])
                tag = False
            elif tt == change[tt] :
                continue
            else:
                if tag ==False:
                    break
        return ''.join(t)

a = Solution()
b = a.maximumNumber( "132", [9,8,5,0,3,6,4,2,6,8])
print("===============",b)
b = a.maximumNumber( "021",[9,4,3,5,7,2,1,9,0,6])
print("===============",b)
b = a.maximumNumber( "334111",[0,9,2,3,3,2,5,5,5,5])
print("===============",b)