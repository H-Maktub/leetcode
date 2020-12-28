class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        current = 0
        for ch in reversed(s):
            num = nums[ch]
            if current <= num:
                current = num
                result = result+num
            else:
                result = result-num
                current = 0
        return result
    
if __name__ == "__main__":
    #106+1100
    a = Solution.romanToInt("",s="MCMXCVI")
    print ('aa',a)
    pass