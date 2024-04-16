class Solution:
    def findLatestTime(self, s: str) -> str:
        t = ''
        for i in range(len(s)):
            ch = s[i]
            if ch == '?':
                if i == 0:
                    if s[1] == '?' or int(s[1]) <= 1:
                        t+='1'
                    else:
                        t+='0'
                if i == 1:
                    if s[0] == '0':
                        t+='9' 
                    else:
                        t+='1'
                if i == 3:
                    t+='5'
                if i == 4:
                    t+='9'
                continue
            t+=ch
        return t
    
a = Solution()
b = a.findLatestTime("??:1?")
print(b)