from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        temp =[]
        def get_value(x,y)->int:
            if x>=len(board) or y>= len(board[0]) or x<0 or y<0:
                return 0
            return board[x][y]
        def s_count(x,y)->int:
            return get_value(x-1,y-1)+get_value(x,y-1)+get_value(x+1,y-1)+get_value(x-1,y)+get_value(x+1,y)+get_value(x-1,y+1)+get_value(x,y+1)+get_value(x+1,y+1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                n = board[i][j]
                r = s_count(i,j)
                if n == 1 and r < 2:
                    temp.append([i,j,0])
                if n == 1 and r > 3:
                    temp.append([i,j,0])
                if n == 0 and r == 3:
                    temp.append([i,j,1])
        for v in temp:
            board[v[0]][v[1]] = v[2]


