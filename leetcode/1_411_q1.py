from collections import Counter
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub = s[i:j+1]
                result = Counter(sub)
                # print(sub,result,result["0"] == k or result["1"] == k)
                if result["0"] <= k or result["1"] <= k:
                    res+=1
        return res

a = Solution()
# b = a.countKConstraintSubstrings("10101",1)
# print(b)
b = a.countKConstraintSubstrings("1010101",2)
print(b)
