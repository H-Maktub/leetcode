from typing import List
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         retList = []
#         for j in range(k):
#             if j == 0:
#                 for i in range(n+1-k):
#                     retList.append([i+1])
#             else:
#                 temp =[]
#                 for nums in retList:
#                     for i in range(nums[j-1],n):
#                         a = nums+[i+1]
#                         temp.append(a)
#                 retList = temp
#             print(retList)          
#         return retList
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        retList = []
        if k==1:
            return [[i+1] for i in range(n)]
        for i in range(n+1-k):      
            temp = self.combine(n-i-1,k-1)
            for nums in temp:
                retList.append(nums+[n-i])
        return retList     

if __name__ == "__main__":
    a = Solution()
    b = a.combine(4,2)
    print('==========',b)
