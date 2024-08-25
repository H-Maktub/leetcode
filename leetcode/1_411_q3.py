class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if k == 1 or k == 9 or k == 3:
            return "9"*n
        if k == 7:
            return "7"*n
        if k == 5 :
            if n < 2:
                return "5"
            return "5"+"9"*(n-2)+"5"
        if k == 2 or k == 4 or k == 8:
            if n < 2:
                return "8"
            return "8"+"9"*(n-2)+"8"
        return 0
for i in range(999999999,-1,-1):
    if i % 7 == 0 and str(i) == str(i)[::-1]:
        print(i)
        break