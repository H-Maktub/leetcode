class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        stack = []
        restult = 0
        temp = 0
        for i in range(len(s)):
            ch = s[i]
            if i>0 and ch == '0' and s[i-1] == '1':
                stack = []
            if ch == '0':
                temp = 0
                stack.append(1)
            if ch == '1':
                if len (stack) != 0:
                    temp += 1
                    stack.pop()
            restult = max(temp,restult)
        return restult*2

a = Solution()
b = a.findTheLongestBalancedSubstring("01000111")
print(b)