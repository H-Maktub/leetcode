from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
if __name__ == "__main__":
    a = Solution()
    b = a.merge([[1,3],[2,6],[8,10],[15,18]])
    print(b)