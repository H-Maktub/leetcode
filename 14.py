from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for tmp in zip(*strs):
            print(tmp)
        if len(strs) ==0:
            return ""
        if len(strs) ==1:
            return strs[0]
        mainStr = strs[0]
        for str in strs:
            if len(mainStr) > len(str):
                mainStr = str
        strs.remove(mainStr)
        max = len(mainStr)
        right = max
        current = 0
        
        while current < right <= max:
            cache = mainStr[:right]
            print(cache)
            result = True
            for str in strs:
                if cache != str[:right]:
                    result = False
                    break
            if result:
                current = right
                right = int(right*1.5+0.5)
                print(result,current,right)
            elif right !=1:
                right = int((right - current)/2+0.5)
                print(result,current,right)
            else:
                right = 0
        return mainStr[:current]
if __name__ == "__main__":
    #106+1100
    a = Solution.longestCommonPrefix("",strs=["dog","racecar","car"])
    print ('aa',a)
    pass