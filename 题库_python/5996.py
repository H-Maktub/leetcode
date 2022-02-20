import re
from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ret = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and i*j%k == 0:
            
                    ret+=1
        return ret
a = Solution()
b = a.countPairs([5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3],7)
print(b)
