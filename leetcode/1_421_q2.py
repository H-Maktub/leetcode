from functools import cache
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        res = 0
        a = ord('a')
        z = ord('z')+1-a
        @cache
        def getLength(c,n)->int:
            new = ord(c)-a+n
            if  new >= z:
                t = new - z
                # print(t)
                return (getLength('a',t)+getLength('b',t))%1000000007
            return 1
        for ch in s:
            res=(res+getLength(ch,t))%1000000007
        return res
    
a = Solution()
b = a.lengthAfterTransformations("jqktcurgdvlibczdsvnsg",7517)
print(b)