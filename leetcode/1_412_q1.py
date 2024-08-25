from typing import List
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums[:]
        nums.sort(reverse=True)
        for i in range(k):
            index = res.index(nums[-1])
            nums[-1] *= multiplier
            res[index] = nums[-1]
            nums.sort(reverse=True)
        return res
a = Solution()
b = a.getFinalState([2,1,3,5,6],5,2)
print(b)