from typing import List
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def run(i,j):
            nonlocal board
            if i < len(board)-1 and board[i+1][j] == 'X':
                while i < len(board):
                    if board[i][j] == '.':
                        break
                    board[i][j] = '.'
                    i+=1
            else:
                 while j < len(board[0]):
                    if board[i][j] == '.':
                        break
                    board[i][j] = '.'
                    j+=1
        ret = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    ret+=1
                    run(i,j)
        return ret
    

a = Solution()
b = a.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
print(b)