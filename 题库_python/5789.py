class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        h1 = int(startTime[:2])
        f1 = int(startTime[3:5])
        h2 = int(finishTime[:2])
        f2 = int(finishTime[3:5])
        if h1 > h2:
            h2+=24
        elif h1 == h2 and f1>f2:
            h2+=24
        result = (h2-h1)*4
        if f1>0:
            result -= f1//15 + (0 if f1%15 == 0 else 1)
        if f2>0:
            result += f2//15
        return result
a = Solution()
b = a.numberOfRounds("12:01","12:44")
print("==============",b)
b = a.numberOfRounds("20:00","06:00")
print("==============",b)
b = a.numberOfRounds("00:00","23:59")
print("==============",b)
b = a.numberOfRounds("00:01","00:00")
print("==============",b)
b = a.numberOfRounds("01:45","15:19")
print("==============",b)
b = a.numberOfRounds("23:46","00:01")
print("==============",b)