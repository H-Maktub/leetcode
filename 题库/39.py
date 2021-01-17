from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        retList = []
        for i,num in enumerate(candidates):
            n = target -num
            if n>0:
                tempList = self.combinationSum(candidates[i:],n)
                for temp in tempList:
                    temp.append(num)
                    retList.append(temp)
            elif n==0:
                retList.append([num])
        return retList


if __name__ == "__main__":
    a = Solution()
    b = a.combinationSum([2,3,6,7],7)
    print('=========',b)
    b = a.combinationSum([2,3,5],8)
    print('=========',b)