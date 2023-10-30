from typing import List 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        l = len(nums)
        result = []
        for i in range(0,l-1):
            left.append(left[i]*nums[i])
            right.insert(0,right[0]*nums[l-1-i])
        for i in range(0,l):
            result.append(left[i] * right[i])
        return result
