class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text += " "
        count = len(text)
        i = 0
        ret = 0
        while i<count:
            ch = text[i]
            if ch in brokenLetters:
                while ch != " ":
                    i+=1
                    ch = text[i]
            elif ch == " ":
                ret+=1
            i+=1
        return ret


a = Solution()
b = a.canBeTypedWords("hello world","ad")
print("=============",b)
