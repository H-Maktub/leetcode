class Solution:
    def minimumSteps(self, s: str) -> int:
        b = 0
        ret = 0
        if s[0] == "1":
            b = 1
        for i in range(1,len(s)):
            ch = s[i]
            if ch == "1":
                b += 1
            else:
                ret+=b
        return ret
a = Solution()
b = a.minimumSteps("101")