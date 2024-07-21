class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        i = 0
        nums = 0
        ret = 0
        while i<n:
            while i<n and s[i] == '0':
                i+=1
            ret += nums
            while i<n and s[i] == '1':
                i+=1
                nums+=1
        return ret