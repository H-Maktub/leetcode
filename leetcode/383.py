from typing import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1 = Counter(ransomNote)
        s2 = Counter(magazine)
        for k in s1:
            if k in s2 and s2[k] >= s1[k]:
                continue
            else:
                return False
        return True
    
a = Solution()
b = a.canConstruct("")