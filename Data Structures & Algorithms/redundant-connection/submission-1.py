class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1] * (n+1)
    def find(self, a):
        curr = a
        while curr!=self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu==pv:
            return False
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu] = self.find(pv)
            self.rank[pv]+=self.rank[pu]
        else:
            self.parent[pv] = self.find(pu)
            self.rank[pu]+=self.rank[pv]
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #find degrees of each node, or DSU where if not union (parents same, ans = that edge)
        #since as we go thru uniting everything, once we get a cycle we are on the last edge
        #of that cycle and thus it is redundant
        uf = DSU(len(edges))
        for u,v in edges:
            if not uf.union(u,v):
                return [u,v]
        