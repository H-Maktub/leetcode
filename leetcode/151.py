class Solution:
    def reverseWords(self, s: str) -> str:
        ret = ""
        temp = ""
        for ch in s:
            if ch == " ":
                if len(temp) > 0:
                    ret = temp + " " + ret
                temp = ""
            else:
                temp += ch
        if len(temp) > 0:
             ret = temp + " " + ret
        ret = ret[0:len(ret)-1]
        return ret
