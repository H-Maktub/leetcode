from typing import List
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        l = len(nums)
        ret = 0
        def isUp(ns)->bool:
            for i in range(1,len(ns)):
                if ns[i] <= ns[i-1]:
                    return False
            return True
        for i in range(l):
            for j in range(i,l):
                t = nums[:i]+nums[j+1:]
                # print(t,nums[i:j+1])
                if len(t) == 0 or  isUp(t):
                    ret +=1
        return ret


a = Solution()
b = a.incremovableSubarrayCount([1,2,3,4])
print(b)

b = a.incremovableSubarrayCount([8,7,6,6])
print(b)