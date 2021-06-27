from typing import List
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        tag = True

        def yan(temp):
            t = True
            for i in range(1,len(temp)):
                if temp[i-1]>= temp[i]:
                    t = False
                    break
            if t:
                return t
        t = True   
        for i in range(1,len(nums)):
            if nums[i-1]>= nums[i]:
                t = False
                temp1 = nums.copy()
                temp1.pop(i-1)
                if yan(temp1):
                    return True
                temp2 = nums.copy()
                temp2.pop(i)
                if yan(temp2):
                    return True
                break
        return t


a = Solution()
b = a.canBeIncreasing([2,3,1,2])
print("===============",b)
b = a.canBeIncreasing([1,2,10,5,7])
print("===============",b)
b = a.canBeIncreasing([105,924,32,968])
print("===============",b)
b = a.canBeIncreasing([1,1])
print("===============",b)
b = a.canBeIncreasing([100,21,100])
print("===============",b)