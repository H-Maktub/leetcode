from typing import Optional
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        pre = {}
        st:TreeNode = None
        def dfs(root:TreeNode):
            nonlocal st
            if root == None:
                return
            if root.val == start:
                st = root
            if root.left != None:
                pre[root.left] = root
                dfs(root.left)
            if root.right != None:
                pre[root.right] = root
                dfs(root.right)
        dfs(root)
        temp = [st]
        ret = -1
        visted = set([st])
        while len(temp) != 0:
            ret+=1
            new = []
            for t in temp:
                if t in pre and pre[t] not in visted:
                    new.append(pre[t])
                    visted.add(pre[t])
                if t.left != None and t.left not in visted:
                    new.append(t.left)
                    visted.add(t.left)
                if t.right != None and t.right not in visted:
                    new.append(t.right)
                    visted.add(t.right)
            temp = new
        return ret
    

a = Solution()
b = a.amountOfTime(TreeNode(1,TreeNode(5),TreeNode(3)),start=3)
print(b)