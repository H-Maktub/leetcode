from typing import List,Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ret = 1
        c = Counter(nums)
        l = sorted(c.keys())
        l_max = max(l)
        # print(l,c)
        for n in l:
            if n > 1 and c[n] > 1:
                i = 1
                new = n
                while new <= l_max:
                    new = new**2
                    count =c.get(new,0)
                    if count > 0:
                        i+=1
                    if count == 1:
                        break
                ret = max(ret,i)
        l1 = c.get(1,0)
        if l1%2 == 0:
            l1-=1
        return max(ret*2-1,l1)
    

a = Solution()
b = a.maximumLength([5,4,1,2,2])
print(b)
b = a.maximumLength([14,14,196,196,38416,38416])
print(b)

b = a.maximumLength([64,25,121,81,49,100,49,36,81,64,25,81,36,36,4,49,81,9,49,100,49,36,100,36,4,49,25,100,25,25,64,4,100,25,16,16,64,144,4,16,25,144,121,9,49,4,100,144,64,36,100,81,4,16,64,64,4,64,25,121,49,49,16,144,36,144,144,25,64,25,100,100,4,16,81,49,4,121,16,100,100,144,9,144,25,9,64,16,36,36,25,64,36,121,64,49,25,81,121,64])
print(b)
