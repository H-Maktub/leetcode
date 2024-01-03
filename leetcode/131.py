from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        t = {}
        def dfs(ds: str) -> List[List[str]]:
            if len(ds) == 1:
                return [[ds]]
            ret = []
            for i in range(len(ds)):
                lefts = ds[:i+1]
                if lefts == lefts[::-1]:
                    rights = ds[i+1:]
                    temp = t.get(rights,None)
                    if not temp:
                        temp = dfs(ds[i+1:])
                        t[rights] = temp
                    for i in temp:
                        a = [lefts]
                        a.extend(i)
                        ret.append(a)
            if ds == ds[::-1] and len(ds) >0:
                ret.append([ds])
            return ret
        return dfs(s)

if __name__ == "__main__":
    a = Solution()
    b = a.partition("cdd")
    print(b)