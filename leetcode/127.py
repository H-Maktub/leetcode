from typing import List
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = [beginWord] + wordList
        temp = collections.defaultdict(set)
        for i in range(len(wordList)):
            for j in range(i+1,len(wordList)):
                c = 0
                for x in range(len(beginWord)):
                    if wordList[i][x] != wordList[j][x]:
                        c +=1
                    if c > 1:
                        break
                if c == 1:
                    temp[wordList[i]].add(wordList[j])
                    temp[wordList[j]].add(wordList[i])
        # print(temp)
        result = [[beginWord]]
        visted = set()
        visted.add(beginWord)
        end = False
        while len(result[-1]) != 0:
            next = []
            for cur in result[-1]:
                for n in temp[cur]:
                    if n not in visted:
                        visted.add(n)
                        next.append(n)
                        if n == endWord:
                            end = True
            result.append(next)
            # print(len(visted),len(result[-1]))
            if end:
                break
        if end == False:
            return 0
        return len(result)
a = Solution()
b = a.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])
print(b)