class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1
        

if __name__ == "__main__":
    a = Solution.strStr("",haystack = "hello", needle = "a")
    print ('aa',a)
    pass