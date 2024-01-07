from typing import List
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        ret = 0
        for i in range(len(nums)):
            if i==0 or  nums[i] == nums[i-1]+1:
                ret+=nums[i]
            else:
                break
        while ret in nums:
            ret+=1
        return ret

a = Solution()
# b = a.missingInteger([1,2,3,2,5])
# print(b)
# b = a.missingInteger([3,4,5,1,12,14,13])
# print(b)

b = a.missingInteger([29,30,31,32,33,34,35,36,37])
print(b)

b = a.missingInteger([46,8,2,4,1,4,10,2,4,10,2,5,7,3,1])
print(b)
b = a.missingInteger([14,9,6,9,7,9,10,4,9,9,4,4])
print(b)