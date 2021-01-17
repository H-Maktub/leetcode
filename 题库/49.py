from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp={}
        for str in strs:
            l = list(str)
            l.sort()
            s="".join(l)
            if s not in temp:
                temp[s]=[]
            temp[s].append(str)
        return list(temp.values())


if __name__ == "__main__":
    a = Solution()
    b = a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(b)