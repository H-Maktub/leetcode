class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        temp =[[root]]
        while temp[-1]:
            temp.append([])
            for t in temp[-2]:
                if t.left:
                    temp[-1].append(t.left)
                if t.right:
                    temp[-1].append(t.right)
        return len(temp)-1