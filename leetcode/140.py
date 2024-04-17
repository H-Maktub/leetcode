from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ret = []
        temp = []
        def dfs(ss:str):
            if len(ss) == 0:
                ret.append(" ".join(temp))
            else:
                for word in wordDict:
                    if ss.startswith(word):
                        temp.append(word)
                        dfs(ss[len(word):])
                        temp.pop()
        dfs(s)
        return ret
    

a = Solution()
b = a.wordBreak("catsanddog",["cat","cats","and","sand","dog"])
print(b)