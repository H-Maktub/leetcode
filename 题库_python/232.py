class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.p1 = []
        self.p2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.p1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.p2:
            while self.p1:
                self.p2.append(self.p1.pop())
        return self.p2.pop()

    def peek(self) -> int:
        if not self.p2:
            while self.p1:
                self.p2.append(self.p1.pop())
        return self.p2[-1]

    def empty(self) -> bool:
       return not self.p1 and not self.p2