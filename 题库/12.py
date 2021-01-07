class Solution:
    def intToRoman(self, num: int) -> str:
        srtList=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        numList=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        retStr = ''
        while num > 0:
            for i in range(len(srtList)):
                while num >= numList[i]:
                    retStr += srtList[i]
                    num -= numList[i]
        return retStr

if __name__ == "__main__":
    a = Solution()
    b =a.intToRoman(20)
    print(b)
   