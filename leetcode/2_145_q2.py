from typing import List
import math
class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        ret = float('inf')
        def run(nums:List[int],X,time):
            nonlocal ret
            if len(nums) == 0:
                ret = min(ret,time)
            else:
                for i in range(len(nums)):
                    # print("=======",i,nums)
                    num = nums[i]
                    run(nums[:i]+nums[i+1:],X+K,time+math.ceil(num/X))
        run(strength,1,0)
        # i = 0
        # print(strength,i,strength[:i],strength[i+1:])
        return ret
    
a = Solution()
b = a.findMinimumTime([3,4,1],1)
print(b)