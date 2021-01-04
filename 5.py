class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxStr = ''
        i = 0
        while i<len(s):
            start=i
            while i<len(s)-1 and s[i] == s[i+1]:
                i +=1
            stop = i
            print(start,stop)
            while start > 0 and stop <len(s)-1 and s[start-1]==s[stop+1]:
                start -= 1
                stop +=1
            print(s[start:stop+1])
            if len(maxStr)<stop+1-start:
                maxStr = s[start:stop+1]
                print(maxStr,stop-start+1)
            i +=1

        return maxStr


if __name__ == "__main__":
    a = Solution()
    b = a.longestPalindrome("aaaaab")
    print('======================',b)
    b = a.longestPalindrome("babad")
    print('======================',b)
    b = a.longestPalindrome("bb")
    print('======================',b)