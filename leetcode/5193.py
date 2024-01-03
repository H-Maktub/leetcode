class Solution:
    def makeFancyString(self, s: str) -> str:
        t = "  "
        for ch in s:
            if  ch == t[-1] and  ch == t[-2]:
                continue
            t+=ch
        return t[2:]


a = Solution()
b = a.makeFancyString("leeetcode")
print(b)

