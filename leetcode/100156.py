from typing import List
import collections
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        temp = [[float('inf')] * 26 for _ in range(26)]
        for i in range(26):
            temp[i][i] = 0
        for i in range(len(original)):
            temp[ord(original[i])-ord('a')][ord(changed[i])-ord('a')] = min(temp[ord(original[i])-ord('a')][ord(changed[i])-ord('a')],cost[i])
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    temp[i][j] = min(temp[i][j],temp[i][k]+temp[k][j])
        ret = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                t = temp[ord(source[i])-ord('a')][ord(target[i])-ord('a')]
                if t == float('inf'):
                    return -1
                else:
                    ret+=t
        return ret
    

a = Solution()
b = a.minimumCost("abcd","acbe",["a","b","c","c","e","d"],["b","c","b","e","b","e"],[2,5,5,1,2,20])
print(b)

# b = a.minimumCost("aaaa","bbbb",["a","c"],["c","b"],[1,2])