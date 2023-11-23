from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in board:
            print(i)
        def dfs(x,y):
            if 0> x  or x >= len(board) or 0> y  or y >= len(board[0]):
                return
            if board[x][y] == "O":
                board[x][y] = "A"
                dfs(x-1,y)
                dfs(x+1,y)
                dfs(x,y-1)
                dfs(x,y+1)
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                if 0 == i  or i == len(board)-1 or 0 == j  or j == len(board[0])-1:
                    if board[i][j] == "O":
                        dfs(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "A":
                    board[i][j] = "O"
                
        

a = Solution()
b = a.solve([["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]])
