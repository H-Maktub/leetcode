from typing import List
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.sort()
        vFences.sort()
        hFences = [1]+hFences+[m]
        vFences = [1]+vFences+[n]
        hl = len(hFences)
        vl = len(vFences)
        h1 = set()
        v1 = set()
        for i in range(1,hl):
            for j in range(i-1,-1,-1):
                # print("----",i,j)
                h1.add(hFences[i]-hFences[j])
        for i in range(1,vl):
            for j in range(i-1,-1,-1):
                # print("----",i,j)
                v1.add(vFences[i]-vFences[j])
        print(v1,h1)
        ret = -1
        for i in  h1:
            if i in v1:
                ret = max(ret,i*i)
        print(ret)
        
        return ret % 1000000007 if ret != -1 else -1

a = Solution()
b = a.maximizeSquareArea(4,3,[2,3],[2])
print(b)
b = a.maximizeSquareArea(6,7,[2],[4])
print(b)

b = a.maximizeSquareArea(3,3,[],[])
print(b)