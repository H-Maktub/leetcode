from typing import Counter, Set, Text
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        t1 = Counter(s)
        t2 = []
        c = 0
        print(set(s))
        l = len(s)
        for i in range(l):
            ch1 = s[i]
            t1[ch1]-=1
            if ch1 not in t2:
                t3 = []
                t2.append(ch1)
                t11 = t1.copy()
                print("============",t1)
                for j in range(i+1,l):
                    ch2 = s[j]
                    t11[ch2] -=1
                    if ch2 not in t3:
                        t3.append(ch2)
                        if t11[ch1] != 0:
                            print(ch1,ch2,t11[ch1])
                            c+=1
                        else:
                            print("=",ch1,ch2,t11[ch2],t11)
                    else:
                        print("-",ch1,ch2,t11[ch2])
        return c


a = Solution()
# b = a.countPalindromicSubsequence("bbcbaba")
# print("==============",b)
b = a.countPalindromicSubsequence("aabca")
print("==============",b)