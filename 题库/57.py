from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        retList = []
        temp = None
        for nums in intervals:
            if temp == None:
                temp = nums
            else:
                if temp[1]<nums[0]:
                    retList.append(temp)
                    temp = nums
                elif temp[1]<nums[1]:
                    temp[1] = nums[1]
                    
        retList.append(temp)
        return retList