class Solution:
    def myAtoi(self, s: str) -> int:
        tmp = {'0','1','2','3','4','5','6','7','8','9'}
        retSrt = ''
        start = 0
        for i in range(len(s)):
            start = i
            if s[i] !=' ':
                if s[i] !='-' or  s[i] !='+':
                    retSrt += s[i]
                break
        start += len(retSrt)
        print(start,s[start:])
        for ch in s[start:]:
            print(ch)
            if ch not in tmp:
                break
            retSrt += ch
        a = 0 
        print(retSrt)
        try:
            a = int(retSrt)
        except:
            pass
        print(a)
        if -2147483648 > a:
            return -2147483648
        if a>2147483647:
            return 2147483647
        return a
if __name__ == "__main__":
    a = Solution()
    b = a.myAtoi('-5-')
    print('======================',b)
    b = a.myAtoi('   -42')
    print('======================',b)
    b = a.myAtoi("4193 with words")
    print('======================',b)