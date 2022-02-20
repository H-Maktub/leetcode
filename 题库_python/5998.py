from typing import List
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        number = finalSum//2
        result = []
        while number>0:
            t = len(result)+1
            number -= t
            result.append(t*2)
        if number < 0:
            t = result.pop() + number*2
            result[-1]+=t
        print(result,number)
        return result
a = Solution()
b = a.maximumEvenSplit(14)