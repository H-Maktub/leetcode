class Solution:
    def sortSentence(self, s: str) -> str:
        temp = s.split(' ')
        ret = [" "]*len(temp)
        for t in temp:
            ret[int(t[-1])-1] = t[:-1]
        return " ".join(ret)

a = Solution()
b =a.sortSentence("is2 sentence4 This1 a3")
print(b)