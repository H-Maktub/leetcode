class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(':')','{':'}','[':']'}
        list = []
        for ch in s:
            if dict.get(ch) != None:
                list.append(dict[ch])
            else:
                if len(list)==0 or list.pop() != ch:
                    return False
        b = bool(len(list))
        return bool(1 - b)

if __name__ == "__main__":
    a = Solution.isValid("",s="()")
    print ('aa',a)
    pass