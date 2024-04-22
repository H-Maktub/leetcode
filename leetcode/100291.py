class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        temp = [0] * 26
        for ch in word:
            i = ord(ch)-ord('a')
            if i >= 0:
                if temp[i] == 0:
                    temp[i] = 1
                elif temp[i] == 2:
                    temp[i] = -1
            else:
                i+=32
                if temp[i] == 1:
                    temp[i] = 2
                elif temp[i] == 0:
                    temp[i] = -1
        res = 0 
        for i in temp:
            if i == 2:
                res+=1
        return res
    
a = Solution()
b = a.numberOfSpecialChars("aaAbcBC")
print(b)
b = a.numberOfSpecialChars("abc")
print(b)
b = a.numberOfSpecialChars("AbBCab")
print(b)