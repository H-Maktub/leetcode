from typing import List
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        t = ""
        for ch in words:
            t+=ch
            if s == t:
                return True
            elif len(s)<len(t):
                return False
        return False
