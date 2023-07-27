from typing import List
from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        temp = Counter(nums).items()
        temp = sorted(temp,key=lambda x:x[1],reverse=True)
        result = []
        for value,count in temp:
            if len(result) == 0:
                result = [[value] for _ in range(count)]
            else:
                for i in range(count):
                    result[i].append(value)
        return result

a = Solution()
b = a.findMatrix([1,3,4,1,2,3,3,3,3,3,1])
print(b)