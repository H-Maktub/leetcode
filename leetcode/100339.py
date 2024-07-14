from typing import List
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        new = ""
        for i in range(n):
            new += s[(i+k)%n]
        return new
    

a = Solution()
b = a.getEncryptedString("dart",3)
print(b)