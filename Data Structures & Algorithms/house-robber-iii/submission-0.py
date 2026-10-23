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
            #take rob option first
            cache[root] = root.val
            if root.left:
                cache[root]+=dfs(root.left.left)+dfs(root.left.right)
            if root.right:
                cache[root]+=dfs(root.right.left)+dfs(root.right.right)
            cache[root] = max(cache[root], dfs(root.left)+dfs(root.right))
            return cache[root]
        return dfs(root)
