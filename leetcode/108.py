from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(l,r):
            if l>r:
                return None
            root_index = (l+r)//2
            root = TreeNode(nums[root_index])
            root.left = build(l,root_index-1)
            root.right = build(root_index+1,r)
            return root
        return build(0,len(nums)-1)

a = Solution()
b = a.sortedArrayToBST([-10,-3,0,5,9])
print(b)