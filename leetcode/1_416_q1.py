from typing import List
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        temp = set(bannedWords)
        c = 0
        for word in message:
            if word in temp:
                c+=1
            if c >= 2:
                break
        return c >= 2