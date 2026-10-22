# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #delete is is the one where we need to shift the left most from the right subtree to top
        if root is None:
            return None
        if key>root.val:
            root.right = self.deleteNode(root.right, key)
        elif key<root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            #root.right becomes the replacement, vice versa. only when theres root.left and right that we do the algo
            if not root.left: return root.right
            elif not root.right: return root.left
            #go as left as we can
            curr = root.right
            while curr.left:
                curr = curr.left
            curr.left = root.left
            res = root.right
            del root
            return res
        return root