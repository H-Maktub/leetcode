class Solution:
    def calculate(self, s: str) -> int:
        temp = [""]
        for ch in s:
            if ch == " ":
                continue
            elif temp[-1].isdigit() and ch.isdigit():
                temp[-1] = str(int(temp[-1])*10+int(ch))
                continue
            temp.append(ch)
        for ch in temp[1:]:
            if temp[-1] == "*":
                temp.pop()
                ch = int(ch) * int(temp.pop())
            elif temp[-1] == "/":
                temp.pop()
                ch = int(int(temp.pop())/int(ch))
            temp.append(ch)
        s = [""]
        for ch in temp[1:]:
            if s[-1] == "+":
                s.pop()
                ch = int(ch) + int(s.pop())
            elif s[-1] == "-":
                s.pop()
                ch = int(s.pop())-int(ch)
            s.append(ch)
        return int(s[-1])

a = Solution()
# b = a.calculate("3+2*2")
# print(b)
# b = a.calculate("3/2")
# print(b)
# b = a.calculate("42")
# print(b)
# b = a.calculate("1227")
# print(b)
# b = a.calculate("0-2147483647")
# print(b)
# b = a.calculate("2*3+4")
# print(b)
b = a.calculate("1*2-3/4+5*6-7*8+9/10")
print(b)