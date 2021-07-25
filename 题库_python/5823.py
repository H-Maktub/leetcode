class Solution:
    def getLucky(self, s: str, k: int) -> int:
        t = ""
        for i in s:
            t+= str(ord(i)-96)
        for _ in range(k):
            tt = 0
            for i in t:
                tt += int(i)
            t= str(tt)
        return int(t)


a = Solution()
b = a.getLucky("zbax",1)
print(b)