class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""
        if columnNumber <= 26:
            return chr(columnNumber-1+ord('A'))
        return self.convertToTitle((columnNumber-1)// 26) + chr((columnNumber-1) % 26+ord('A'))
    

a = Solution()
b = a.convertToTitle(1)
print(b)
b = a.convertToTitle(701)
print(b)
b = a.convertToTitle(52)
print(b)