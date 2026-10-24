# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #serialize into "length(delimiter)preorderinorder"
        preorder = []
        def dfsp(root):
            nonlocal preorder
            if root is None:
                preorder.append("NULL")
                return
            preorder.append(root.val)
            dfsp(root.left)
            dfsp(root.right)
        dfsp(root)
        preorder = serializedString = ",".join(map(str, preorder))
        print(preorder)
        return preorder
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #deserialize from converting preorder+inorder
        #into binary tree
        deserialized = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if deserialized[i]=="NULL":
                i+=1
                return None
            root = TreeNode(int(deserialized[i]))
            i+=1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
        