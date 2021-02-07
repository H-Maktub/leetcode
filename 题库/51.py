from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        t = []
        retList = []
        def dfs(i):
            if i==n:
                retList.append([])
                for num in t:
                    p = list("."*n)
                    p[num] = 'Q'
                    retList[-1].append(''.join(p))
                return
            s = set()
            for x,val  in enumerate(t):
                s.add(val)
                s.add(val+i-x)
                s.add(val-i+x)
            temp = []
            for v in range(n):
                if v not in s:
                    temp.append(v)
            for num in temp:
                t.append(num)
                dfs(i+1)
                t.pop()
        dfs(0)
        return retList

        

if __name__ == "__main__":
    a = Solution()
    b = a.solveNQueens(4) #[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    print(b)