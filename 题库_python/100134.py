# a、e、i、o、u
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        u = ['a','e','i','o','u']
        ret = 0
        for i in range(len(s)):
            x=y=0
            for j in range(i+1,len(s),2):
                c = s[j-1:j+1]
                print(s[i:j+1],c)
                for ch in c:
                    if ch in u:
                        x+=1
                    else:
                        y+=1
                if x==y and x*y%k == 0:
                    ret+=1
        return ret

a = Solution()
b = a.beautifulSubstrings("baeyh",2)
print(b)