class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu==pv:
            return False
        if self.rank[pu]<self.rank[pv]:
            self.parents[pu] = pv
            self.rank[pv]+=self.rank[pu]
        else:
            self.parents[pv] = pu
            self.rank[pu]+=self.rank[pv]
        return True
        
    def find(self, a):
        while self.parents[a] != a:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #dsu / labeling with dfs/bfs
        uf = DSU(n)
        count = 0
        for u,v in edges:
            uf.union(u,v)
        seen = set()
        for i in range(n):
            if uf.find(i) not in seen:
                count+=1
                seen.add(uf.find(i))
        return count