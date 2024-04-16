from typing import List
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        temp = [2,3,5,7]
        for i in range(8,101):
            result = True
            for j in temp:
                if i % j == 0:
                    result = False
                    break
            if result:
                temp.append(i)
        res = []
        for i in range(len(nums)):
            if nums[i] in temp:
                res.append(i)
        if len(res) < 2:
            return 0
        return res[-1] - res[0]
a = Solution()
b = a.maximumPrimeDifference([4,2,9,5,3])
print(b)