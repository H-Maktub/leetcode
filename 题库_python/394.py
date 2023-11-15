class Solution:
    def decodeString(self, s: str) -> str:
        temp = []
        for c in s:
            if c == "]":
                t = ""
                
                while temp[-1] != "[":
                    t = temp[-1]+t
                    temp.pop()
                temp.pop()
                s = ""
                while len(temp) > 0 and temp[-1].isdigit():
                    s = temp[-1]+s
                    temp.pop()
                s = int(s)
                temp.append(t*s)
            else:
                temp.append(c)
        return ''.join(temp)
    
a = Solution()
b = a.decodeString("3[a]2[bc]")
print(b)
b = a.decodeString("3[a2[c]]")
print(b)
b = a.decodeString("2[abc]3[cd]ef")
print(b)
b = a.decodeString("100[leetcode]")
print(b)