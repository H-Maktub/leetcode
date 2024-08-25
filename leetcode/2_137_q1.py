from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        def isUp(nums:List[int])->bool:
            for i in range(1,len(nums)):
                if nums[i] - nums[i-1] != 1:
                    return False
            return True
        for i in range(len(nums)-k+1):
            new = nums[i:i+k]
            # print(new,isUp(new))
            if isUp(new):
                res.append(new[-1])
            else:
                res.append(-1)
        return res
    

a = Solution()
b = a.resultsArray([1,2,3,4,3,2,5],3)
print(b)
b = a.resultsArray([1,3,4],2)
print(b)