class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        retStr = ''
        i = 0
        n = numRows*2-2
        while i< numRows:
            retStr += s[i]
            if i ==0 or i*2==n:
                tmp = i+n
                while tmp<len(s):
                    retStr += s[tmp]
                    tmp +=n
            else:
                tmp = i+n-2*i
                while tmp<len(s):
                    retStr += s[tmp]
                    if tmp+2*i<len(s):
                        retStr += s[tmp+2*i]
                    tmp +=n
            i +=1
        return retStr

if __name__ == "__main__":
    a = Solution()
    b = a.convert("LEETCODEISHIRING",1)
    print('======================',b)
    b = a.convert("AB",1)
    print('======================',b)