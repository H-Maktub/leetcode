from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        temp = [-1]
        res = []
        for i in range(len(nums)):
            if nums[i] - temp[-1] == 1:
                temp.append(nums[i])
            else:
                temp = [nums[i]]
            if i >= k-1:
                if len(temp) >= k:
                    res.append(temp[-1])
                else:
                    res.append(-1)
        return res
    
a = Solution()
b = a.resultsArray([1,2,3,4,3,2,5],3)
print(b)
b = a.resultsArray([1,3,4],2)
print(b)
b = a.resultsArray([1],1)
print(b)