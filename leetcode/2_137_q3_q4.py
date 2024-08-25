from typing import List
class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        temp = []
        for i in range(m):
            for j in range(n):
                temp.append([board[i][j],i,j])
        temp.sort(reverse=True)
        # print(temp)
        res = float('-inf')
        for x in range(m*n-2):
            xv = temp[x]
            for y in range(x+1,m*n-1):
                yv = temp[y]
                test = xv[0]+yv[0]+temp[y+1][0]
                if res >= test:
                    break
                if xv[1] == yv[1] or xv[2] == yv[2]:
                    continue
                for z in range(y+1,m*n):
                    zv = temp[z]
                    new = xv[0]+yv[0]+zv[0]
                    if res >= new:
                        break
                    if xv[1] == zv[1] or xv[2] == zv[2] or yv[1] == zv[1] or yv[2] == zv[2]:
                        continue
                    res = max(new,res)
                    # print(new)
                    break
                        # return res
        return res

a = Solution()
# b = a.maximumValueSum([[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]])
# print(b)
b = a.maximumValueSum([[82,24,11],
                       [95,91,-8],
                       [-89,-30,-29]])
print(b)