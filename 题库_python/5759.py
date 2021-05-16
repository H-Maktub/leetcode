from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = []
        for num in nums:
            a = [num]
            for t in total:
                a.append(t^num)
            total.extend(a)       
        return sum(total)

a = Solution()
b = a.subsetXORSum([1,3])
print(b)
b = a.subsetXORSum([5,1,6])
print(b)