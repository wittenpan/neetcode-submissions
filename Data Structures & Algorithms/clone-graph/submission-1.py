"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        #oldToNew again..
        oldToNew = {}
        stk = [node]
        visited = set([node])
        while stk:
            nd = stk.pop()
            oldToNew[nd] = Node(nd.val)
            for nei in nd.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)
        stk = [node]
        visited = set([node])
        while stk:
            nd = stk.pop()
            for nei in nd.neighbors:
                oldToNew[nd].neighbors.append(oldToNew[nei])
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)
        return oldToNew[node]

