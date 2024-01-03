from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        t = set([str(x) for x in range(1,10)])
        all = []
        for i,temp in enumerate(board):
            for j,num in enumerate(temp):
                if num != ".":
                    if num in rows[i]:
                        return False
                    else:
                        rows[i].add(num)

                    if num in columns[j]:
                        return False
                    else:
                        columns[j].add(num)
                    n = i//3*3+j//3
                    # print(n,i+1,i//3,(j+1)//3)
                    if num in boxes[n]:
                        return False
                    else:
                        boxes[n].add(num)
                else:
                    all.append([i,j])
        tempall = 0 
        while len(all) != tempall:
            tempall = len(all)
            for i,j in all:
                if board[i][j] == ".": 
                    n = i//3*3+j//3
                        
                    # print(t)
                    p =t.difference(rows[i],columns[j],boxes[n])
                    # print("++++++++++",i,j,p,all)
                    if len(p)==1:
                        print("============",i,j,p,t,rows[i],columns[j],boxes[n])
                        a = p.pop()
                        rows[i].add(a)
                        columns[j].add(a)
                        boxes[n].add(a)
                        board[i][j]=a
                        all.remove([i,j])
                        for i,temp in enumerate(board):
                            print(temp)
        valid = False
        def dfs(x):
            print(x)
            nonlocal valid
            if x == len(all):
                valid = True
                return
            i,j = all[x]
            n = i//3*3+j//3
            p =t.difference(rows[i],columns[j],boxes[n])
            for a in p:
                board[i][j] = a
                rows[i].add(a)
                columns[j].add(a)
                boxes[n].add(a)
                dfs(x+1)

                if valid:
                    return
                else:
                    board[i][j] = "."
                    rows[i].remove(a)
                    columns[j].remove(a)
                    boxes[n].remove(a)
        dfs(0)

if __name__ == "__main__":

#     ['5', '1', '9', '7', '4', '8', '6', '3', '2']
# ['7', '8', '3', '6', '5', '2', '4', '1', '9']
# ['4', '2', '6', '1', '3', '9', '8', '7', '5']
# ['3', '5', '7', '9', '8', '6', '2', '4', '1']
# ['2', '6', '4', '3', '1', '7', '5', '9', '8']
# ['1', '9', '8', '5', '2', '4', '3', '6', '7']
# ['9', '7', '5', '8', '6', '3', '1', '2', '4']
# ['8', '3', '2', '4', '9', '1', '7', '5', '6']
# ['6', '4', '1', '2', '7', '5', '9', '8', '3']
    a = Solution()
    c=[
        [".",".","9","7","4","8",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        [".","2",".","1",".","9",".",".","."],
        [".",".","7",".",".",".","2","4","."],
        [".","6","4",".","1",".","5","9","."],
        [".","9","8",".",".",".","3",".","."],
        [".",".",".","8",".","3",".","2","."],
        [".",".",".",".",".",".",".",".","6"],
        [".",".",".","2","7","5","9",".","."]]
#     c=[
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
    b = a.solveSudoku(c)
    print("-------------------------")
    for i,temp in enumerate(c):
        print(temp)