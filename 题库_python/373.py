from typing import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)
        temp = [(nums1[i]+nums2[0],i,0) for i in range(min(n1,k))]
        ret = []
        for i in range(k):
            _,x,y = heapq.heappop(temp)
            ret.append([nums1[x],nums2[y]])
            if y+1<n2:
                heapq.heappush(temp,(nums1[x]+nums2[y+1],x,y+1))
            if len(temp)==0:
                break
        return ret
    
a = Solution()
b = a.kSmallestPairs([1,2],[3],3)
print(b)