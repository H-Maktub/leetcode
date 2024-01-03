class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l = len(part)
        temp = []
        for ch in s:
            temp.append(ch)
            if ch == part[-1]:
                if len(temp) >= l:
                    n = len(temp)-l
                    if "".join(temp[n:]) == part:
                        temp = temp[:n]
        return "".join(temp)

        

a = Solution()
b = a.removeOccurrences("daabcbaabcbc","abc")
print("==============",b)
a = Solution()
b = a.removeOccurrences("axxxxyyyyb","xy")
print("==============",b)