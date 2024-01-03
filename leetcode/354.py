from typing import List
import bisect
# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         envelopes.append([0,0])
#         envelopes.sort(key=lambda x: (x[0], x[1]))
#         print(envelopes)
#         temp = [0]
#         for i in range(1,len(envelopes)):
#             t=i
#             s = []
#             while t:
#                 t-=1
#                 if envelopes[t][0]<envelopes[i][0] and envelopes[t][1]<envelopes[i][1]:
#                     s.append(temp[t]+1)
#             temp.append(max(s)) 
#         return max(temp)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
            print(f)
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num
        
        return len(f)
if __name__ == "__main__":
    a = Solution()
    b = a.maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81]])
    print(b)
    b = a.maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]])
    print(b)
    