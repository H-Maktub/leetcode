from typing import List
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        temp = sorted(maximumHeight,reverse=True)
        for i in range(1,len(temp)):
            while temp[i] >= temp[i-1]:
                temp[i] = temp[i-1] - 1
            if temp[i] <= 0:
                return -1
        return sum(temp)