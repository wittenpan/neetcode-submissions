# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if root==subRoot:
        #check left and right
        #do an and
        ans = False
        def dfs(root, subRoot):
            nonlocal ans
            ans |= isSameTree(root, subRoot)
            if root:
                dfs(root.left, subRoot)
                dfs(root.right, subRoot)
        
        def isSameTree(root, subRoot):
            if root and subRoot:
                if root.val!=subRoot.val:
                    return False
                return isSameTree(root.left,subRoot.left) and isSameTree(root.right,subRoot.right)
            elif root or subRoot:
                return False
            else:
                return True
        dfs(root, subRoot)
        return ans 