#优化方式，固定长度滑动
from typing import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        ret = ""
        n = len(s)
        m = len(t)
        ts = Counter(t)
        tempts = Counter()
        def matchCounter(l):
            for i in ts:
                if l[i]<ts[i]:
                    return False
            return True
        for i in range(n):
            if ts[s[i]]:
                left=i
                right=i
                break
                
        for i in range(left,n):
            if ts[s[i]] and not matchCounter(tempts):
                tempts[s[i]]+=1
                m-=1
                # print(s[i])
                # ts.remove(s[i])
            if matchCounter(tempts):
                right = i
                ret = s[left:right+1]
                print(left,right,ret,i,ts,tempts)
                break
        # print(ts,tempts)
        while left<right:

            while left<right:
                temp = s[left]
                if ts[temp]:
                    if matchCounter(tempts):
                        print("+++++lefttstr",s[left:right+1])
                        if right+1-left<len(ret):
                            ret=s[left:right+1]
                        tempts[temp]-=1
                    else:
                        # print("+++++lefttstr2222",s[left:right+1])
                        break
                left+=1
            print("111111",left,n,right,s[left:right+1])
            if right == n:
                break
            right+=1
            while right<n:
                temp = s[right]
                if ts[temp]:
                    tempts[temp]+=1
                    if matchCounter(tempts):
                        print("+++++rightstr",s[left:right+1])
                        # return
                        break
                right+=1
        return ret
if __name__ == "__main__":
    a = Solution()
    b = a.minWindow("ADOBECODEBANC","ABC")
    print('==========',b)
    b = a.minWindow("ab","b")
    print('==========',b)
    b = a.minWindow("bba","ab")
    print('==========',b)