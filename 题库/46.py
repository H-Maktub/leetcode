from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        retList = []
        for num in nums:
            temp = []
            n = len(retList)
            if n==0:
                retList=[[num]]
                continue
            n=len(retList[0])
            for i in range(n+1):
                
                for tempList in retList:
                    p = tempList.copy()
                    p.insert(i,num)
                    temp.append(p)
            # print(temp)
            retList = temp
        return retList

if __name__ == "__main__":
    a = Solution()
    b = a.permute([1,2,3])
    print('=====',b,len(b))
    b = a.permute([5,4,6,2])
    print('=====',b,len(b))