class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        temp = set()
        res = set()
        for ch in word:
            t = ord(ch)-ord('A')
            if t < 26 and t+32 in temp:
                res.add(t)
            else:
                if t-32 in temp:
                    res.add(t-32)
            temp.add(t)
        return len(res)



a = Solution()
b = a.numberOfSpecialChars("abBCab")
print(b)
