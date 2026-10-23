# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #once we go left, the upper b becomes the root val
        #once we go right, the lb becomes root val.
        res = True
        def dfs(root, ub, lb):
            nonlocal res
            if not root:
                return
            if root.val<=lb or root.val>=ub:
                res &= False
                return
            dfs(root.left, root.val,lb)
            dfs(root.right,ub,root.val)
        dfs(root,float('inf'),float('-inf'))
        return res