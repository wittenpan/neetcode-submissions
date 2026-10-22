# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root):
            if root is None:
                return 0
            nonlocal res
            l, r = dfs(root.left), dfs(root.right)
            if abs(r-l)>1:
                res = False
            return max(l,r)+1
        dfs(root)
        return res