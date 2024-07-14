from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ret = []
        def addNum(root,i):
            if root == None:
                return
            if len(ret) < i+1:
                ret.append([])
            ret[i].append(root.val)
            for ch in root.children:
                addNum(ch,i+1)
        addNum(root,0)
        return ret