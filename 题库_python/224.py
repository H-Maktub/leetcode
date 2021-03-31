class Solution():
    def calculate(self, s):
        res, num, sign = 0, 0, 1
        stack = []
        
        for ch in s:
            if ch.isdigit():
                num = 10 * num + int(ch)
            elif ch == "+" or ch == "-":
                res += sign * num
                num = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res

                 
a= Solution()
b = a.calculate("(1+(4+5+2)-3)+(6+8)")
print(b)

