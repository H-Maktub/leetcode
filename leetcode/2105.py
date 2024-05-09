from typing import List
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l = 0
        r = len(plants)-1
        ll = capacityA
        rr = capacityB
        ret = 0
        while l <= r:
            if l == r:
                if plants[l] > ll and plants[r] > rr:
                    ret+=1
                break
                    
            if plants[l] > ll:
                ll = capacityA
                ret+=1
            if plants[r] > rr:
                rr = capacityB
                ret+=1
            ll -= plants[l]
            rr -= plants[r]
            l+=1
            r-=1
        return ret
    

a = Solution()
b = a.minimumRefill([2,2,3,3],5,5)
print(b)
b = a.minimumRefill([2,1,1],2,2)
print(b)