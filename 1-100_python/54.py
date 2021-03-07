from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        retList = []
        m = len(matrix)
        n = len(matrix[0])
        run = min((m+1)//2,(n+1)//2)
        print(m,n,run)
        for i in range(run):
            if i == n-1-i:
                for a in range(i,m-i):
                    print(a)
                    retList.append(matrix[a][i])
                break
            if i == m-i-1:
                retList.extend(matrix[i][i:n-i])
                break
            retList.extend(matrix[i][i:n-1-i])
            for temp in matrix[i:m-i-1]:
                retList.append(temp[n-1-i])
            retList.extend(matrix[m-1-i][i+1:n-i][::-1])
            for temp in matrix[i+1:m-i][::-1]:
                retList.append(temp[i])
        return retList


if __name__ == "__main__":
    a = Solution()
    b = a.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
    print('=======',b)
    b = a.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])
    print('=======',b)
    b = a.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [13,14,15,16]
])
    print('=======',b)
    b = a.spiralOrder([[3],[2]])
    print('=======',b)
    b = a.spiralOrder([[1]])
    print('=======',b)
    b = a.spiralOrder([[6,9,7]])
    print('=======',b)
    b = a.spiralOrder([
        [2,3,4],
        [5,6,7],
        [8,9,10],
        [11,12,13],
        [14,15,16]])
    print('=======',b)
    b = a.spiralOrder([
        [1,11],
        [2,12],
        [3,13],
        [4,14],
        [5,15],
        [6,16],
        [7,17],
        [8,18],
        [9,19],
        [10,20]])
    print('=======',b)
    