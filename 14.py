from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mainStr = strs[0]
        
        for str in strs:
            if len(mainStr) > len(str):
                mainStr = str
        strs.remove(mainStr)
        right = len(mainStr)
        current = 0
        
        while current != right:
            cache = mainStr[:right]
            result = True
            for str in strs:
                if cache != str[:right]:
                    result = False
                    break
            if result:
                right = current//2 + right//2
                current = right
            else:
                right = right//2

        
        return mainStr[:right]
if __name__ == "__main__":
    #106+1100
    a = Solution.longestCommonPrefix("",strs=["flower","flow","flight"])
    print ('aa',a)
    pass