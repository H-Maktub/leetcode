# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         temp = [0]
#         ret = 0
#         t=1
#         for i,ch in enumerate(s):
#             if ch =="(":
#                 t+=1
#                 temp.append(i+1)
#             else:
#                 t-=1
#                 temp.pop()
#             if t == 0:
#                 temp.append(i+1)
#                 t=1
#             else:
#                 ret = max(ret,i+1-temp[-1])
#         return ret

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        if l == 0:return 0
        temp=[0] *l
        for i in range(1,l):
            if s[i] == ")" and s[i-1] =="(":
                temp[i] = temp[i-2]+2
            elif s[i] == ")" and s[i-1] ==")" and i-temp[i-1]-1>=0 and s[i-temp[i-1]-1]=="(":
                temp[i]= temp[i-1]+temp[i-temp[i-1]-2]+2
        print(temp)
        return max(temp)
if __name__ == "__main__":
    a = Solution()
    b = a.longestValidParentheses("(()")#2
    print("=====",b)
    b = a.longestValidParentheses(")()())")#4
    print("=====",b)
    b = a.longestValidParentheses("()(()")#2
    print("=====",b)
    b = a.longestValidParentheses(")")#0
    print("=====",b)
    b = a.longestValidParentheses(")()())")#4
    print("=====",b)
    b = a.longestValidParentheses("(()(((()")#2
    print("=====",b)
    b = a.longestValidParentheses("()")#2
    print("=====",b)
    b = a.longestValidParentheses("()(())")#6
    print("=====",b)