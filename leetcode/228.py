from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []
        for i in range(len(nums)):
            if i == 0 or ret[-1][1] - nums[i] != -1:
                ret.append([nums[i],nums[i]])
            else:
                ret[-1][1] = nums[i]
        for i in range(len(ret)):
            a = ret[i][0]
            b = ret[i][1]
            if a == b:
                ret[i] = str(b)
            else:
                ret[i] = str(a)+"->"+str(b)
        return ret