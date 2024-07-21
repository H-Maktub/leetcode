class Solution:
    def doesAliceWin(self, s: str) -> bool:
        t = set(['a','e','i','o','u'])
        nums = 0
        for ch in s:
            if ch in t:
                nums+=1
        if nums == 0:
            return False
        if nums % 2 == 1:
            return True
        return True
a = Solution()
b = a.doesAliceWin("leetcoder")
print(b)