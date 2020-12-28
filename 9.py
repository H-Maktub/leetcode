class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

if __name__ == "__main__":
    a = Solution.isPalindrome("",x=0)
    print ('aa',a)
    pass