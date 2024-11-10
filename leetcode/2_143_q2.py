from typing import List
from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        new = set()
        for num in nums:
            new.add(num)
            new.add(num-k)
            new.add(num+k)
        new = list(new)
        new.sort()
        nums.sort()
        c = Counter(nums)
        res = 1
        left = 0
        right = 0
        n = len(nums)
        for num in new:
            while left < n and nums[left]+k < num:
                left+=1
            while right < n and  nums[right]-k <= num:
                right+=1
            r = c[num]+min(numOperations,right-left-c[num])
            # print(c[num+k],num+k,min(numOperations-1,bright-bleft-c[num+k]))
            res = max(r,res)
            # print(num,r,nums[left])
        return res
    
a = Solution()
b = a.maxFrequency([601735,478312,280664,808082,333905,231916,120671,961759,246778,381702,935676,259026,338468,954821,276626,162553,373003,770478,657560,37818,696358,351320,387613,57063,76812,49569,410066,153766,60337,783839,675790,394602,28679,550896,579276,177971,916123,360736,23752,374690,877638,556129,48005,496009,730168,919729,463581,96670,969839,957031,772857,303311,287917,782795,974228,997079,387506,552391,203328,424393,558016,971764,232590,202572,124199,937722,399289,786780,683214,762488,888579,171906,298393,776413,859779,604302,242435,532673,173527,702835,828310,241380,487311,177735,37612,40959,871610,397345,99873,7576,80586,435329,226112,925822,698656,737714,898874,439517,61963,264364],
                   327459,54)
print(b)
b = a.maxFrequency([93,45],1,2)
print(b)