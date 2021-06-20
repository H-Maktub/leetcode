class Solution:
    def largestOddNumber(self, num: str) -> str:

        for i in range(len(num)-1,-1,-1):
            if int(num[i]) %2 != 0:
                return num[:i+1]
        return ""
a = Solution()
b = a.largestOddNumber("52")
print("===============",b)
b = a.largestOddNumber("4206")
print("===============",b)
b = a.largestOddNumber("35427")
print("===============",b)