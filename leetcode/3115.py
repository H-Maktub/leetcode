from typing import List
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        temp = set([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73, 79,83,89,97])
        ret = 0
        pre = None
        for i in range(len(nums)):
            num = nums[i]
            if num in temp:
                if pre == None:
                    pre = i
                else:
                    ret = i - pre
        return ret