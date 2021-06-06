from typing import List
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        n = len(boxes)
        m = len(packages)
        packages.sort()
        temp = [float('inf') for _ in range(n+1)]
        tempbox = [[float('inf')]]
        while boxes:
            box = boxes.pop()
            if len(box)==1 and box[-1]>=packages[-1]:
                tempbox[0][0] = min(tempbox[0][0],box[-1])
            elif len(box)>1:
                tempbox.append(box)
        boxes = tempbox
        n = len(boxes)
        for i in range(n):
            box = boxes[i]
            box.sort()
            if box[-1]>=packages[-1]:
                x = len(box)-1
                temp[i] = 0
                for j in range(m-1,-1,-1):
                    package = packages[j]
                    while x>-1 and package<=box[x]:
                        x-=1
                    x+=1
                    temp[i]+=box[x]-package
                    if temp[i]>=temp[i-1]:
                        temp[i] = temp[i-1]
                        break
                    
        if min(temp) == float('inf'):
            return -1
        return min(temp) % 1000000007
    
a = Solution()
b = a.minWastedSpace()
print(b)


