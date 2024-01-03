from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
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
        return True


if __name__ == "__main__":
    a = Solution()
    b = a.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])
    print(b)