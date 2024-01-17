from  typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        l = [0] * n
        r = [0] * n
        l[0] = nums[0]
        r[n-1] = nums[n-1]
        for i in range(1,n):
            l[i] = min(l[i-1],nums[i])
            r[n-1-i] = max(r[n-i],nums[n-1-i])
        for i in range(1,n-1):
            if l[i-1] < nums[i] < r[i+1]:
                return True
        return False

a = Solution()
b = a.increasingTriplet([20,100,10,12,5,13])