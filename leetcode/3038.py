class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums)//2:
            if nums[0]+nums[1] == nums[i*2]+nums[i*2+1]:
                i+=1
            else:
                break
        return i