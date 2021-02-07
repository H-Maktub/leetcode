from typing import List
class Solution:
    def totalNQueens(self, n: int) -> int:
        t = []
        ret = 0
        def dfs(i):
            nonlocal ret
            if i==n:
                ret+=1
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
        return ret

        

if __name__ == "__main__":
    a = Solution()
    b = a.totalNQueens(4) #[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    print(b)