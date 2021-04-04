class Solution:
    def removeDuplicates(self, S: str) -> str:
        temp= [""]
        for ch in S:
            if ch == temp[-1]:
                temp.pop()
            else:
                temp.append(ch)
        return ''.join(temp)
