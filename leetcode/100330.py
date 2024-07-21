from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        t = Counter(s)
        ret = 0
        for v,c in t.items():
            if c % 2 == 1:
                ret+=1
            else:
                ret+=2
        return ret
            

a = Solution()
b = a.minimumLength("abaacbcbb")
print(b)
