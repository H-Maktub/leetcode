class Solution:
    def minTimeToType(self, word: str) -> int:
        t = 0
        result = 0
        for s in word:
            s = ord(s)-ord("a")
            r = abs(s-t)
            if r >=13:
                r=abs(r-26)
            result+=1+r
            t=s
        return result

a = Solution()
b = a.minTimeToType("abc")
print("===========",b)
b = a.minTimeToType("bza")
print("===========",b)
b = a.minTimeToType("zjpc")
print("===========",b)