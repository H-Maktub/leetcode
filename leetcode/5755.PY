class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        ret = 0
        for i in range(l//2):
            ret = max(ret,nums[i]+nums[-i-1])
        return ret