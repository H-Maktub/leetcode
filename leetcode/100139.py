from typing import List
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        for i in range(len(mat)):
             for j in range(n):
                if i % 2 == 0:
                    if mat[i][j] != mat[i][(j+k)%n]:
                        print("======",i,mat[i],(i+k)%n,mat[(i+k)%n])
                        return False
                else:
                     if mat[i][j] != mat[i][(n+j-k%n)%n]:
                        print("======")
                        return False
        return True

a = Solution()
b = a.areSimilar([[1,2,1,2],[5,5,5,5],[6,3,6,3]],2)
print(b)