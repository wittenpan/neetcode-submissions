# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #max of depth of left + depth of right
        res = 0
        def dfs(root):
            nonlocal res
            if root is None:
                return 0
            l, r = dfs(root.left),dfs(root.right)
            res = max(res, l+r)
            return 1+max(l,r)
        dfs(root)
        return res