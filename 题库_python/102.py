from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        temp =[[root]]
        ret = [[root.val]]
        while temp[-1]:
            temp.append([])
            ret.append([])
            for t in temp[-2]:
                if t.left:
                    temp[-1].append(t.left)
                    ret[-1].append(t.left.val)
                if t.right:
                    temp[-1].append(t.right)
                    ret[-1].append(t.right.val)
        return ret[:-1]