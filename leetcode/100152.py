class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        temp = []
        ret = 0
        for ch in word:
            if len(temp) == 0 or abs(ord(temp[-1])-ord(ch)) <= 1:
                temp.append(ch)
            else:
                ret += len(temp)//2
                temp = [ch]
            print(temp)
        ret += len(temp)//2
        return ret
    

a = Solution()
# b = a.removeAlmostEqualCharacters("aaaaa")
# print(b)

# b = a.removeAlmostEqualCharacters("abddez")
# print(b)

# b = a.removeAlmostEqualCharacters("zyxyxyz")
# print(b)

b = a.removeAlmostEqualCharacters("acb")
print(b)