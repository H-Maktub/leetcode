from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        temp =[0]*26
        for i,ch in enumerate(s):
            temp[ord(ch)-ord('a')] = i
        result = []
        start=0
        end=0
        for i,ch in enumerate(s):
            end = max(end,temp[ord(ch)-ord('a')])
            if i == end:
                result.append(end-start+1)
                start = end+1
        return result