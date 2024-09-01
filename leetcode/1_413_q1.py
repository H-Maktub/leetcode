class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        a = ord(coordinate1[0])-ord('a')+int(coordinate1[1])
        b = ord(coordinate2[0])-ord('a')+int(coordinate2[1])
        if a % 2 == b % 2:
            return True
        return False