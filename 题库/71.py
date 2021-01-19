class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = path.split("/")
        retList = []
        for str in temp:
            if str=="..":
                if len(retList):
                    retList.pop()
            elif str !="" and str !=".":
                retList.append(str)      
        return "/"+"/".join(retList)
if __name__ == "__main__":
    a = Solution()
    b = a.simplifyPath("/a/../../b/../c//.//")
    print(b)
    b = a.simplifyPath("/a//b////c/d//././/..")
    print(b)
    b = a.simplifyPath("/home/")
    print(b)