from typing import List
from collections import Counter
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        t = []
        n = len(nums)
        c = Counter()
        for i in range(n//2):
            x = abs(nums[i]-nums[n-1-i])
            t.append(x)
            c[x]+=1
        # print(t,c)
        tops = c.most_common()
        ret = 2 * 100000
        for top in tops:
            # print("==========",top)
            res= 0
            for i in range(n//2):
                if t[i] != top[0]:
                    a = min(nums[i],nums[n-1-i])
                    b = max(nums[i],nums[n-1-i])
                    wu = top[0]-t[i]
                    res+=1
                    # print(i,a,b,wu)
                    if a - wu < 0 and b + wu > k: 
                        res+=1
                if res > ret:
                    break
            # print("---------",res)
            ret = min(res,ret)
            if ret == n//2 - top[1]:
                break
        return ret


a = Solution()
b = a.minChanges([1,0,1,2,4,3],4)
print(b) #2
b = a.minChanges([0,1,2,3,3,6,5,4],6)
print(b) #2
b = a.minChanges([1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0],1)
print(b) # 4
b = a.minChanges([9,2,7,7,8,9,1,5,1,9,4,9,4,7],9)
print(b) #4
b = a.minChanges([5,6,0,3,3,2,0,4,6,4],6)
print(b) #3
b = a.minChanges([1,1,1,1,0,0,0,5,4,3,19,17,16,15,15,15,19,19,19,19],20)
print(b) #7