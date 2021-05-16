from typing import List
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        temp = [["."] * m for _ in range(n)] 
        for x in range(m):
            index = n-1
            for y in range(n-1,-1,-1):
                if box[x][y] == "*":
                    temp[y][m-x-1] = "*"
                    index = y-1
                elif box[x][y] == "#":
                    temp[index][m-x-1] = "#"
                    index -=1
        return temp

a = Solution()
b = a.rotateTheBox([["#","#","*",".","*","."],
            ["#","#","#","*",".","."],
            ["#","#","#",".","#","."]])
for i in b:
    print(i)
