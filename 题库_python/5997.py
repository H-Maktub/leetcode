from typing import List
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3 == 0:
            t = num//3
            return [t-1,t,t+1]
        return []
a = Solution()
b = a.sumOfThree(33)
print(b)