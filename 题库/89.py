from typing import List
# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         if n == 0:
#             return[0]
#         if n == 1:
#             return [0,1]
#         nums = self.grayCode(n-1)
#         l = len(nums)
#         a = 2**(n-1)
#         for i in range(l):
#             nums.append(nums[l-1-i]+a)
#         return nums

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return[0]
        if n == 1:
            return [0,1]
        retList =[0,1]
        val = 1
        for i in range(1,n):
            val = val*2
            l = len(retList)
            for j in range(l):
                retList.append(retList[l-j-1]+val)
        return retList
if __name__ == "__main__":
    a = Solution()
    b = a.grayCode(2)
    print(b)