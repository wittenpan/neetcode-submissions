"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        #create 2d prefix sum grid for quick isSame calculations for isLeaf things.
        #recursive func that returns root of that tree.
        leafNodes = {
            0: Node(False, True),
            1: Node(True, True)
        }
        n = len(grid)
        def recurse(r,c,n) -> 'Node':
            if n==1:
                return leafNodes[grid[r][c]]
            n//=2
            topLeft = recurse(r,c,n)
            topRight = recurse(r,c+n,n)
            bottomLeft = recurse(r+n,c,n)
            bottomRight = recurse(r+n,c+n,n)
            #if all are leaves and all have same val, we return one of the nodes as the parent
            if (topLeft.isLeaf and topRight.isLeaf and
                bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return topLeft
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        return recurse(0,0,n)
