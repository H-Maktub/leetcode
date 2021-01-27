from typing import List, NoReturn
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        retList = []
        worddict = Counter(words)
        n = len(words)
        if n == 0:
            return []
        l = len(words[0])
        sl = len(s)
        i=0
        temp = Counter()
        for i in range(l):
            t = i
            a = i
            wordcount = 0
            temp.clear()
            while a+l <=sl:
                one = s[a:a+l]
                if worddict.get(one,0)==0:
                    temp.clear()
                    wordcount = 0
                    t = a+l
                else:
                    temp[one] = temp.get(one,0)+1
                    wordcount+=1
                while temp.get(one,0)> worddict[one]:
                    w = s[t:t+l]
                    temp[w] = temp.get(w,0)-1
                    wordcount-=1
                    t = t+l
                if wordcount == n:
                    retList.append(t)
                a = a+l
        return retList

if __name__ == "__main__":
    a = Solution()
    # b = a.findSubstring("barfoothefoobarman",["foo","bar"])
    # print("aaaaaaaaaaa",b)
    # b = a.findSubstring("wordgoodgoodgoodbestword",["word","good","best","word"])
    # print("aaaaaaaaaaa",b)
    # b = a.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"])
    # print("aaaaaaaaaaa",b)
    b = a.findSubstring("aaaaaaaaaaaaaa",["aa","aa"])
    print("aaaaaaaaaaa",b)