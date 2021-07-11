from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        Row = len(maze)
        Col = len(maze[0])
        
        Q = []
        Q.append(entrance)
        maze[entrance[0]][entrance[1]] = '+'
        step = 0
        while Q:
            step += 1
            t = []
            for _ in range(len(Q)):
                r, c = Q.pop()
                
                for nr, nc in [[r-1,c], [r+1,c], [r, c-1], [r,c+1]]:
                    if 0 <= nr < Row and 0 <= nc < Col:
                        if maze[nr][nc] == '.':
                            if nr in (0, Row - 1) or nc in (0, Col - 1):
                                print(nr,nc)
                                return step
                            maze[nr][nc] = '+'
                            t.append([nr, nc])
            Q = t
        
        return -1


a = Solution()
b = a.nearestExit([
    ["+","+",".","+"],
    [".",".",".","+"],
    ["+","+","+","."]],[1,2])
print("==================",b)
b = a.nearestExit([
    ["+",".","+","+","+","+","+"],
    ["+",".","+",".",".",".","+"],
    ["+",".","+",".","+",".","+"],
    ["+",".",".",".","+",".","+"],
    ["+","+","+","+","+",".","+"]],[3,2])
print("==================",b)
b = a.nearestExit([[".","+"]],[0,0])
print("==================",b)
