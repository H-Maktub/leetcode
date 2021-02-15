from typing import ByteString
class Solution:
    def isNumber(self, s: str) -> bool:
        temp = {"0","1","2","3","4","5","6","7","8","9"}
        temp2 = {"+","-"}
        s = s.lower()
        nums = s.split("e")
       
        def isnum(n,m) -> bool:
            if len(n)>0 and n[0] in temp2:
                n = n[1:]
            if  n == "" or n ==".":
                return False
            ns = n.split(".")
            if len(ns) >m:
                return False
            ret = True
            for i in range(len(ns)):
                    for c in ns[i]:
                        if c not in temp:
                            return False
            return ret
        if len(nums)>2 or len(nums)==0:
            return False
        ret  = isnum(nums[0],2)
        if len(nums)==2:
            ret = ret and isnum(nums[1],1)
        return ret

if __name__ == "__main__":
    a = Solution()
    b = a.isNumber("+6e-1")
    print(b)
    b = a.isNumber(".")
    print(b)
    b = a.isNumber(".1")
    print(b)