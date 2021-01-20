from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ret =False
        n = len(word)
        v1 = len(board)
        h1 = len(board[0])
        def found(i,j,s)->List:
            retList=[]
            if i>0 and (i-1,j) not in s:
                retList.append([i-1,j])
            if j>0 and (i,j-1) not in s:
                retList.append([i,j-1])
            if i<v1-1 and (i+1,j) not in s:
                retList.append([i+1,j])
            if j<h1-1 and (i,j+1) not in s:
                retList.append([i,j+1])
            return retList
        def next(x,i,j,tmp)-> bool:
            if x==n:
                return True
            f = found(i,j,tmp)
            for i,a in enumerate(f):
                if board[a[0]][a[1]] == word[x]:
                    t = tmp.copy()
                    t.add((a[0],a[1]))
                    if next(x+1,a[0],a[1],t):
                        return True
        for i,temp in enumerate(board):
            for j,num in enumerate(temp):
                if num == word[0]:
                    
                    tmpSet = set()
                    tmpSet.add((i,j))
                    if next(1,i,j,tmpSet):
                        return True
        return ret

if __name__ == "__main__":
    a = Solution()
    b = a.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],"ABCCED")
    print(b)
    b = a.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],"SEE")
    print(b)
    b = a.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],"ABCB")
    print(b)
    b = a.exist([["a","a"]],"aaa")
    print(b)
    b = a.exist([
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]],
        "ABCESEEEFS")
    print(b)