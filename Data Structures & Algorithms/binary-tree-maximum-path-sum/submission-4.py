# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #again postorder traversal
        #res = max(res, l+r+root.val)
        res = root.val
        def dfs(root):
            nonlocal res
            if root is None:
                return 0
            l, r = max(0,dfs(root.left)), max(0,dfs(root.right))
            res = max(res, l+r+root.val)
            return root.val + max(l,r)
        dfs(root)
        return res