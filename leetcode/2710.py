class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        while len(num) > 0 and num[-1] == "0":
            num = num[:-1]
        return num
    
a = Solution()
b = a.removeTrailingZeros("51230100")
print(b)
b = a.removeTrailingZeros("31514216007864075756059111751787923413952537015859352242147727420")
print(b)