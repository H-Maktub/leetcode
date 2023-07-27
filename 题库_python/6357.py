from typing import List
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        result = []
        oldqueries = queries
        nums.sort()
        queries.sort()
        temp = [0 for _ in range(len(nums))]
        for i in range(len(queries)):
            q = queries[i]
            sums = 0
            if i == 0:
                for j in range(len(nums)):
                    temp[j] = q - nums[j]
                    sums = abs(temp[j])
            elif queries[i] == queries[i-1]:
                sums = result[-1]
            else:
                
            result.append(sum(sums))
        return result

a = Solution()
b = a.minOperations([3,1,6,8],[1,5])
print(b)