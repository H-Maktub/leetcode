from typing import List
import math
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        n1 = math.ceil(n/2)
        m1 = math.ceil(m/2)
        temp = [0]*3 #[1,1][0,2]
        retn = 0
        for i in range(m1):
            for j in range(n1):
                a = grid[i][j]
                b = grid[i][n-j-1]
                c = grid[m-1-i][j]
                d = grid[m-1-i][n-j-1]
                # print(i,j,a,b,c,d)
                res = [0,0]
                if i == m-1-i and j == n-1-j and a == 1:
                    retn+=1
                    continue
                if i != m-1-i and j != n-1-j:
                    res[a]+=1
                    res[c]+=1 
                    res[b]+=1
                    res[d]+=1   
                elif i != m-1-i:
                    res[a]+=1
                    res[c]+=1 
                elif j != n-1-j:
                    res[a]+=1
                    res[b]+=1 
                    
                if sum(res) == 4:
                    retn+=min(res)
                else:
                    # print(res,a,b,c,d)
                    temp[res[1]]+=1
        print(temp,retn)
        a = temp[2]%2
        if a == 0:
            retn+=temp[1]
        else:
            if temp[1] >= 1:
                retn+=temp[1]
            else:
                retn+=2
        return retn

a = Solution()
b = a.minFlips([[1,0,0],[0,1,0],[0,0,1]])
print("====",b) #3
b = a.minFlips([[0,1],[0,1],[0,0]])
print("====",b)#2
b = a.minFlips([[1],[1]])
print("====",b)#2
b = a.minFlips([[1,1,1]])
print("====",b)#3
b = a.minFlips([[0,0,1],[1,1,1]])
print("====",b)#2
b = a.minFlips([[1],[1],[1],[0]])
print("====",b)#2
                    
                    

                


