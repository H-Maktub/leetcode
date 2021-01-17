from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        retList = []
        all = 0
        for num in candidates:
            all+=num
        print('-----',all,candidates)
        for i,num in enumerate(candidates):
            if i>0 and candidates[i] == candidates[i-1]:
                all -=num
                continue
            print("aa",num)
            if all<target:
                break
            if all == target:
                retList.append(candidates[i:])
                print("========",candidates,retList,all,target)
                break
            n = target -num
            if n>0 and target<=all:
                tempList = self.combinationSum2(candidates[i+1:],n)
                print(tempList,n)
                for temp in tempList:
                    temp.append(num)
                    retList.append(temp)
            elif n==0:
                retList.append([num])
            all-=num
        return retList


if __name__ == "__main__":
    # a = [2,5,2,1,2]
    a = Solution()
    b = a.combinationSum2([1],1)
    print('=========',b)
    b = a.combinationSum2([2,2,2],4)
    print('=========',b)
    b = a.combinationSum2([2,1,3,1,4],10)
    print('=========',b)
    b = a.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],27)
    print('=========',b)