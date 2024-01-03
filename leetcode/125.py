class Solution:
    def isPalindrome(self, s: str) -> bool:
        ret = ""
        for c in s:
            c = c.lower()
            if c.isalnum():
                ret+=c
        return ret == ret[::-1]