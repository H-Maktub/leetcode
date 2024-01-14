from typing import List
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a1 = []
        b1 = []
        al = len(a)
        bl = len(b)
        sl = len(s)
        for i in range(sl):
            if i+al<=sl and s[i:i+al] == a:
                a1.append(i)
            if i+bl<=sl and s[i:i+bl] == b:
                b1.append(i)
        ret = set()
        # print(a1,b1)
        l = 0
        r = 0
        for i in a1:
            while l < len(b1):
                # print(b1[l],i)
                if i - b1[l] < 0:
                    break
                if i - b1[l] > k:
                    l+=1
                    continue
                if i-b1[l] <= k:
                    ret.add(i)
                    break
            while r < len(b1):
                if b1[r]- i < 0:
                    r+=1
                    continue
                if b1[r] - i > k:
                    break
                if  b1[r]-i <= k:
                    ret.add(i)
                    break
        return sorted(list(ret))

a = Solution()
# b = a.beautifulIndices("isawsquirrelnearmysquirrelhouseohmy","my","squirrel",15)
# print(b)
# b = a.beautifulIndices("abcd","a","a",4)
# print(b)
# b = a.beautifulIndices("frtzggff","g","f",1)
# print(b) #[5]
b = a.beautifulIndices("ocmm","m","oc",3)
print(b) #[5]
b = a.beautifulIndices("jqcdc","c","d",2)
print(b) #[5]