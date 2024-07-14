from typing import List
from functools import cache
class Trie:
    def __init__(self) -> None:
        self.nodes = {}
        self.end = False
        self.cost = 10**8
    def insert(self,word:str,cost:int):
        curr = self
        for ch in word:
            if ch not in curr.nodes:
                curr.nodes[ch] = Trie()
            curr = curr.nodes[ch]
        curr.end = True
        curr.cost = min(cost,curr.cost)
            
    def find(self,s:str)->List[List]:
        ret = []
        curr = self
        for i in range(len(s)):
            ch = s[i]
            if ch not in curr.nodes:
                break
            if curr.nodes[ch].end:
                ret.append([s[i+1:], curr.nodes[ch].cost])
            curr = curr.nodes[ch]
        return ret
            

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        temp = Trie()
        n = len(words)
        for i in range(n):
            temp.insert(words[i],costs[i])
        n = len(target)
        @cache
        def dp(i)->int:
            if i == n:
                return 0
            ret = 10**8
            cur = temp
            for j in range(i,n):
                if target[j] not in cur.nodes:
                    break
                cur = cur.nodes[target[j]]
                if cur.end:
                    ret = min(ret,cur.cost+dp(j+1))
            return ret
        ans = dp(0)
        if dp(0) == 10**8:
            return -1
        return ans


a = Solution()
b = a.minimumCost("abcdef",["abdef","abc","d","def","ef"],[100,1,1,10,5])
print(b)
b = a.minimumCost("aaaaa",["a"],[10000])
print(b)