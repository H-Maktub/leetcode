class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split(' ')
        s = pattern
        if len(s) != len(t):
            return False
        temp1 = {}
        temp2 = {}
        for i in range(len(s)):
            if s[i] not in temp1 and t[i] not in temp2:
                temp1[s[i]] = t[i] 
                temp2[t[i]] = s[i] 
                     
            else:
                if s[i] not in temp1 or t[i] not in temp2:
                    return False
                if temp1[s[i]] != t[i] or temp2[t[i]] != s[i]:
                    return False
        return True