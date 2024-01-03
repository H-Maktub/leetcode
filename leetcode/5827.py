from typing import List
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        t = "B"
        if color == t:
            t = "W"
        def found(x,y,r,c,s):
            x+=r
            y+=c
            if 0<=x<8 and 0<=y<8:
                if board[x][y] == s:
                    return True
                elif board[x][y] == ".":
                    print("2",x,y)
                    return False
                else:
                    return found(x,y,r,c,s)
            else:
                print("1",x,y)
                return False
        if rMove>0 and board[rMove-1][cMove] == t and found(rMove,cMove,-1,0,color):
            return True
        if rMove<7 and board[rMove+1][cMove] == t and found(rMove,cMove,1,0,color):
            return True
        if cMove>0 and board[rMove][cMove-1] == t and found(rMove,cMove,0,-1,color):
            return True
        if cMove<7 and board[rMove][cMove+1] == t and found(rMove,cMove,0,1,color):
            return True

        if rMove>0 and cMove>0 and board[rMove-1][cMove-1] == t and found(rMove,cMove,-1,-1,color):
            return True
        if rMove<7 and cMove<7 and board[rMove+1][cMove+1] == t and found(rMove,cMove,1,1,color):
            return True
        if rMove<7 and cMove>0 and board[rMove+1][cMove-1] == t and found(rMove,cMove,1,-1,color):
            return True
        if rMove>0 and cMove<7 and board[rMove-1][cMove+1] == t and found(rMove,cMove,-1,1,color):
            return True
        return False

a = Solution()
# b = a.checkMove( [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]],4,3,"B")
# print("=========",b)
# b = a.checkMove([
#     ["W","W",".","B",".","B","B","."],
#     ["W","B",".",".","W","B",".","."],
#     ["B","B","B","B","W","W","B","."],
#     ["W","B",".",".","B","B","B","."],
#     ["W","W","B",".","W",".","B","B"],
#     ["B",".","B","W",".","B",".","."],
#     [".","B","B","W","B","B",".","."],
#     ["B","B","W",".",".","B",".","."]],7,4,"B")
# print("=========",b)
b = a.checkMove([
    ["B","W",".","B","W","W","B","."],
    ["B",".",".","B","W","W",".","."],
    ["W","W",".","B","B",".","B","W"],
    ["B","W","B",".","B",".","B","B"],
    ["B","W","W","B",".","W","B","B"],
    ["W","W",".","B","W","B",".","."],
    ["W",".","B","W","W","B",".","B"],
    ["W",".","B","B",".","B",".","."]]
,2
,5
,"B")
print("=========",b)