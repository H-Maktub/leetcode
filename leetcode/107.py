from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        temp = []
        def order(root:TreeNode,i):
            if root != None:
                if len(temp) <= i:
                    temp.append([])
                temp[i].append(root.val)
                order(root.left,i+1)
                order(root.right,i+1)
        order(root,0)
        print(temp)
        return temp[::-1]