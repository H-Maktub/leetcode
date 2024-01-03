from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroPoint = None
        current = 0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                if zeroPoint == None:
                    zeroPoint = i
            else:
                if zeroPoint != None:
                    nums[zeroPoint] = nums[i]
                    nums[i] = 0
                    zeroPoint += 1



