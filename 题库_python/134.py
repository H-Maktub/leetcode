from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        cur = 0
        while cur < l:
            l1=0
            cnt=0
            while cnt < l:
                j = (cur+cnt)%l
                l1 += gas[j]-cost[j]
                if l1<0:
                    break
                cnt+=1
            if cnt == l:
                return cur
            else:
                cur=cur+cnt+1
        return-1