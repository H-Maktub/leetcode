class MinStack:

    def __init__(self):
        self.mlist = []
        self.slist = []
    def push(self, val: int) -> None:
        if len(self.mlist) == 0:
            self.mlist.append(val)
        else:
            self.mlist.append(min(self.mlist[-1],val))
        self.slist.append(val)

    def pop(self) -> None:
        self.slist.pop()
        self.mlist.pop()

    def top(self) -> int:
        return self.slist[-1]

    def getMin(self) -> int:
        return self.mlist[-1]

a = MinStack()
a.push(-2)
a.push(0)