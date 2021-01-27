class Solution:
    def longestValidParentheses(self, s: str) -> int:
        temp = [0]
        t = 0
        ret = 0
        for i,ch in enumerate(s):
            if ch =="(":
                temp.append(temp[i]+1)
            else:
                t-=1
                temp.append(temp[i]-1)
        print(temp)
        return ret

if __name__ == "__main__":
    a = Solution()
    b = a.longestValidParentheses("(()")
    print("=====",b)
    b = a.longestValidParentheses(")()())")
    print("=====",b)
    b = a.longestValidParentheses("()(()")
    print("=====",b)