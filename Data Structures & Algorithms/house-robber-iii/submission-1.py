# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #house robber recurrence relation:
        #max of (rob this house, choose not to rob)
        #which is (house val + dp[i-2], dp[i-1])
        #how to keep dp arr....
        #we only need to keep dp[i-2], dp[i-1]
        #choose to rob or not rob
        #this is only one path, how to make it entire tree???
        cache = {None:0}
        def dfs(root):
            if root in cache:
                return cache[root]
            l, r, gl, gr = 0,0,0,0
            if root.left:
                gl = dfs(root.left.left) + dfs(root.left.right)
                l = dfs(root.left)
            if root.right:
                gr = dfs(root.right.left) + dfs(root.right.right)
                r = dfs(root.right)
            cache[root] = max(l+r, gl+gr+root.val)
            return cache[root]
        return dfs(root)
