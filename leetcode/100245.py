from typing import Counter
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                result = Counter(s[i:j+1])
                if max(result.values()) <= 2:
                    ret = max(ret,j+1-i)
        return ret
    

a = Solution()
b = a.maximumLengthSubstring("bcbbbcba")
print(b)