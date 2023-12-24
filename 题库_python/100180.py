from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ret = 0
        nums.sort()
        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]

        for i in range(n-1,1,-1):
            if pre[i-1] > nums[i]:
                return pre[i]
        return -1
    

a = Solution()
b = a.largestPerimeter([5,5,5])
print(b)

b = a.largestPerimeter([1,12,1,2,5,50,3])
print(b)

b = a.largestPerimeter([5,5,50])
print(b)