# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p is None and q) or (q is None and p):
            return False
        #could but insert Nones bfs
        res = True
        def dfs(p,q):
            nonlocal res
            if p.val!=q.val:
                res = False
            if p.left and not q.left:
                res = False
            if q.left and not p.left:
                res = False
            if q.right and not p.right:
                res = False
            if p.right and not q.right:
                res = False
            if q.left and p.left:
                dfs(p.left,q.left)
            if q.right and p.right:
                dfs(p.right,q.right)
        dfs(p,q)
        return res
