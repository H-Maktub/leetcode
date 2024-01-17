from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        t = sorted(nums)
        n = len(nums)
        c = (n+1)//2-1
        r = n-1
        for i in range(0,n,2):
            nums[i] = t[c]
            if i+1<n:
                nums[i+1] = t[r]
            r-=1
            c-=1
