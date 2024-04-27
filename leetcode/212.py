from typing import List
import collections
class Trie:
    def __init__(self) -> None:
        self.child = collections.defaultdict(Trie)
        self.word = None
    def insert(self,word:str):
        cur = self
        for c in word:
            cur = cur.child[c]
        cur.word = word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        temp = Trie()
        for word in words:
            temp.insert(word)
        res = set()
        def dfs(now, i1, j1):
            ch = board[i1][j1]
            if ch not in now.child:
                return
            now = now.child[ch]
            if now.word != None:
                res.add(now.word)
            board[i1][j1] = "#"
            for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    dfs(now, i2, j2)
            board[i1][j1] = ch
            
        m,n = len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(temp,i,j)
        return list(res)