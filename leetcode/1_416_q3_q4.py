class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        source = [0]*26
        cur = [0]*26
        res = [0]
        def cmp(a,b)->bool:
            for i in range(26):
                if a[i] > b[i]:
                    return False
            return True
        for i in range(len(word2)):
            source[ord('a')-ord(word2[i])]+=1
        j = 0
        for i in range(len(word1)):
            cur[ord('a')-ord(word1[i])]+=1
            res.append(res[-1])
            if i >= len(word2)-1 and cmp(source,cur):
                c = 0
                while cmp(source,cur):
                    c+=1
                    cur[ord('a')-ord(word1[j])]-=1
                    j+=1
                res[-1]+=c
        # print(res)
        return sum(res)


a = Solution()
# b = a.validSubstringCount("abcabc","abc")
# print(b)
b = a.validSubstringCount("dcbdcdccb","cdd")
print(b)