# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        #keep track of maxval seen so far
        def dfs(root,maxVal):
            nonlocal res
            if root is None:
                return
            if root.val>=maxVal:
                res+=1
                maxVal = root.val
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
        dfs(root,float('-inf'))
        return res
