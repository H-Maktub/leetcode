from typing import Counter, List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        map = Counter(p)
        l = len(p)
        temp = None
        result = []
        for i in range(0,len(s)-l+1):
            if i == 0:
                temp = Counter(s[0:l])
            elif s[i-1] != s[i+l-1]:
                temp.update({s[i-1]:-1,s[i+l-1]:1})
            if map == temp:
                result.append(i)
        return result

a = Solution()
b = a.findAnagrams("cbaebabacd","abc")