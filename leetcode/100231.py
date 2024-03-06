class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ret = 0
        for num in nums:
            if num < k:
                ret+=1
        return ret