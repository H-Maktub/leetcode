# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if int(s) ==0:
#             return 0
#         n = len(s)
#         if n==1:
#             if s != "0":
#                 return 1
#             else:
#                 return 0
#         if n == 2:
#             if s[0] == "0":
#                 return 0
#             if "0" in s:
#                 return 1
#             elif int(s)<=26:
#                 return 2
#             else:
#                 return 1
#         a = 0
#         if s[n-1:] != "0":
#             a += self.numDecodings(s[:n-1])
#         if s[n-2:][0] != "0" and int(s[n-2:])<=26:
#             a += self.numDecodings(s[:n-2])
#         print(a)
#         return a
class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s) ==0 or s[0] =="0":
            return 0
        n =len(s)
        if n ==1:
            return 1
        temp = [1 for _ in range(n+1)]
        for i in range(2,n+1):
            temp[i] = 0
            if s[i-1] != "0":
                temp[i] += temp[i-1]
            num = s[i-2:i]
            if 26>=int(num)>=10:
                temp[i] += temp[i-2]
        return temp[-1]

if __name__ == "__main__":
    a = Solution()
    b = a.numDecodings("12")#2
    print("========",b)
    b = a.numDecodings("226")#3
    print("========",b)
    b = a.numDecodings("1")#1
    print("========",b)
    b = a.numDecodings("1201234")#3
    print("========",b)
    b = a.numDecodings("01")#0
    print("========",b)
    b = a.numDecodings("11111111111111111111111")
    print("========",b)