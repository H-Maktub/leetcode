from typing import List 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k = k % l
        new = nums[l-k:l]+nums[0:l-k]
        for i in range(0,l):
            nums[i] = new[i]
        print(nums)
a = Solution()
b = a.rotate([1,2,3,4,5,6,7],3)