class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        l = 0
        for i in range(length):
            if s[length-i-1] != ' ':
                l =  l+1
            elif l>0:
                return l
        return l

if __name__ == "__main__":
    b = Solution()
    a = b.lengthOfLastWord(s = "    ")#3
    print ('aa',a)
    a = b.lengthOfLastWord(s = "a")#3
    print ('aa',a)
    a = b.lengthOfLastWord(s = " a")#3
    print ('aa',a)
    a = b.lengthOfLastWord(s = "Hello World")#3
    print ('aa',a)
    pass