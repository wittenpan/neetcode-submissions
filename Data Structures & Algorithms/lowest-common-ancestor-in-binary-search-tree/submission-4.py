# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #check if l, r has both p and q or root ==pq and left/r contains other
        #dfs because it goes as deep as possibl
        #res to keep track
        def dfs(root, p,q):
            if root is None:
                return None
            if root==p or root==q:
                return root
            l, r = dfs(root.left,p,q), dfs(root.right,p,q)
            if l and r:
                return root
            return l or r
        return dfs(root,p,q)