from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        temp = {}
        m = 0
        for i in range(len(nums)):
            num = nums[i]
            if num not in temp:
                temp[num] = []
            temp[num].append(i)
            m = max(m,num)
        li = temp[m]
        print(li)
        ret = 0
        pre = 0
        for i in range(k-1,len(li)):
            t = 0
            if i > k-1:
                t = pre*(li[i]-li[i-1]-1)
            pre = li[i-(k-1)] + 1
            ret+=pre+t
            print("====",i,ret,pre,t)
        ret+=pre * (len(nums)-1-li[-1])
        return ret
    
a = Solution()

b = a.countSubarrays([1,3,2,3,1,3],2)#224
print(b)
# b = a.countSubarrays([61,23,38,23,56,40,82,56,82,56,82],2)#224
# print(b)
b = a.countSubarrays([61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82],2)#224
print(b)

