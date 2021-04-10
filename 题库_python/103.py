from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        temp =[[root]]
        ret = [[root.val]]
        tag = False
        while temp[-1]:
            tag = not tag
            temp.append([])
            ret.append([])
            for t in temp[-2]:
                if t.left:
                    temp[-1].append(t.left)
                if t.right:
                    temp[-1].append(t.right)
            if tag:
                for t in temp[-1][::-1]:
                    ret[-1].append(t.val)
            else:
                for t in temp[-1]:
                    ret[-1].append(t.val)
        return ret[:-1]