class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder+","
        n = len(preorder)
        i = 0
        t = 1
        while i < n:
            if t == 0:
                return False
            ch = preorder[i]
            if ch == ",":
                if preorder[i-1]!="#":
                    t-=1
                else:
                    t+=1
            i+=1
        return not t

a = Solution()
b =a.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
print(b)
b =a.isValidSerialization("1,#")
print(b)
b =a.isValidSerialization("9,#,#,1")
print(b)