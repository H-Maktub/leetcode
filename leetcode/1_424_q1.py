from typing import List
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        all = sum(nums)
        ret = 0
        temp = 0
        for num in nums:
            temp += num
            if num == 0:
                if temp == all-temp:
                    ret+=2
                if temp == all-temp+1:
                    ret+=1
                if temp == all-temp-1:
                    ret+=1
        return ret
a = Solution()
b = a.countValidSelections([1,0,2,0,3])
print(b)
        