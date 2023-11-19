class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        l = min(len(s1),len(s2),len(s3))
        result = -1
        for i in range(l):
            if s1[i] == s2[i] == s3[i]:
                result = i
            else:
                break
        if result == -1:
            return -1
        return len(s1)+len(s2)+len(s3)-3*(result+1)
a = Solution()
b = a.findMinimumOperations("abc","abb","ab")
print(b)

b = a.findMinimumOperations("a","a","a")
print(b)

b = a.findMinimumOperations("oby","obz","obf")
print(b)