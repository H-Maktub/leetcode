from typing import Coroutine


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a = ord(coordinates[0])-96
        b = int(coordinates[1])
        c = a+b
        if c%2:
            return True
        else:
            return False

a = Solution()
b = a.squareIsWhite("a1")
print(b)
b = a.squareIsWhite("h3")
print(b)
b = a.squareIsWhite("c7")
print(b)
