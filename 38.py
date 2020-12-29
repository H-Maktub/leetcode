class Solution:
    def countAndSay(self, n: int) -> str:
        retstr = '1'
        for i in range(n-1):
            cache = ''
            ch_c =''
            ch_num = 0
            for ch in retstr:
                if ch_c == ch:
                    ch_c = ch
                    ch_num  = ch_num +1
                else:
                    if ch_num > 0:
                        cache = cache+ str(ch_num)+ch_c
                    ch_c =ch
                    ch_num = 1
            cache = cache + str(ch_num)+ch_c
            retstr = cache
        return retstr

if __name__ == "__main__":
    a = Solution()
    for i in range(5):
        b = a.countAndSay(  n=i+1)
        # print('aa',b)
    pass