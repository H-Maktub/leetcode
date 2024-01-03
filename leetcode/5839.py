from typing import List
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles.sort(reverse=True)
        ret = sum(piles)
        while k!=0:
            t = piles[0]
            s = t//2
            ret-=s
            t=t-s
            piles[0] =t
            print(s,piles)
            if len(piles)>k:
                piles=piles[:k]
            for i in range(1,len(piles)):
                if t>=piles[i]:
                    piles[0] = piles[i]
                    piles[i] = t
                    break
                elif i == len(piles):
                    
            
            k-=1
        return ret

a = Solution()
b = a.minStoneSum([4,3,6,7],3)
print("========",b)