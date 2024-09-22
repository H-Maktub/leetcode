class Solution:
    def convertDateToBinary(self, date: str) -> str:
        temp = date.split("-")
        res = []
        for t in temp:
            num = int(t)
            res.append(f'{num:b}')
        return '-'.join(res)
    
a = Solution()
b = a.convertDateToBinary("2080-02-29")