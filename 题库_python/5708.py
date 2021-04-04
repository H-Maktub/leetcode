from typing import List
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        temp={}
        ret = 0
        for num in nums:
            key = num-int(str(num)[::-1])
            if temp.get(key,None) != None:
                ret += temp[key]
                temp[key]+=1
            else:
                print(num,key)
                temp[key]=1
        return ret%1000000007
       
