from typing import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        t =  Counter(s)
        temp = 0
        for value in t.values():
            if temp !=0 and temp != value:
                return False
            temp = value
        return True


a = Solution()
b = a.areOccurrencesEqual("abababa")
print(b)