from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        t = {"+","-","*","/"}
        temp = []
        for ch in tokens:
            if ch in t:
                b = temp.pop()
                a = temp.pop()
                c = 0
                if ch == "+":
                    ch = a+b
                elif ch == "-":
                    ch = a-b
                elif ch == "*":
                    ch = a*b
                elif ch == "/":
                    ch = int(a/b)
            temp.append(int(ch))
            
        return temp[-1]

if __name__ == "__main__":
    a = Solution()
    b = a.evalRPN(["2","1","+","3","*"])
    print(b)
    b = a.evalRPN(["4","13","5","/","+"])
    print(b)
    b = a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(b)