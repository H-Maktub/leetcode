class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ret = 0
        n = len(columnTitle)
        for i in range(n):
            ch = columnTitle[i]
            num = ord(ch) - ord('A') + 1
            ret+= 26**(n-i-1)*num
        return ret

a = Solution()
b = a.titleToNumber("A")
print(b)