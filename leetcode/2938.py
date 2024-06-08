class Solution:
    def minimumSteps(self, s: str) -> int:
        o=i=0
        om=im=0
        for ch in s:
            if ch == '0':
                im+=i
                o+=1
            else:
                om+=o
                i+=1
        print(o,i,om,im)
        return im

a = Solution()
b = a.minimumSteps("101")
print(b)