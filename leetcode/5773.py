class Solution:
    def maxValue(self, n: str, x: int) -> str:
        l = len(n)
        if n [0] != "-":
            for i in range(l):
                if int(n[i]) < x:
                    return n[:i]+str(x)+n[i:]
        else:
            for i in range(1,l):
                if int(n[i]) > x:
                    return n[:i]+str(x)+n[i:]
        return n+str(x)

a = Solution()
b = a.maxValue("89",9)
print(b)
b = a.maxValue("-13",2)
print(b)
b = a.maxValue("-132",3)
print(b)
b = a.maxValue("-6484681536456",5)
print(b)
b = a.maxValue("469975787943862651173569913153377",3)
print(b)