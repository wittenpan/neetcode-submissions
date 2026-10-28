class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, u):
        curr = u
        while self.parent[curr]!=curr:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu==pv: return False
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu] = pv
            self.rank[pv]+=self.rank[pu]
        else:
            self.parent[pv] = pu
            self.rank[pu]+=self.rank[pv]
        return True
        
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        #undir connected
        #generate all MSTs?
        #keep track of which edges appear in all MSTs and which edges don't
        #brute force generate all MSTs
        #prims or kruskals
        #a critical edge appears in every single MST
        #a pseudo critical edge appears in some
        for i, e in enumerate(edges):
            e.append(i)  # [v1, v2, weight, original_index]
        edges.sort(key=lambda x:x[2])
        mst_weight = 0
        uf = DSU(n)
        for v1, v2, w, i in edges:
            #this works because if you can successfully union two connected components..
            #bc weights in sorted order
            if uf.union(v1, v2):
                mst_weight+=w
        critical, pseudo = [], []
        for n1, n2, edge_weight, i in edges:
            #try with current edge to find critical
            weight = 0
            uf = DSU(n)
            for v1, v2, w, j in edges:
                if i!=j and uf.union(v1,v2):
                    weight+=w
            if max(uf.rank)!=n or weight>mst_weight:
                critical.append(i)
                continue
            #pseudo
            uf = DSU(n)
            uf.union(n1,n2)
            weight = edge_weight
            for v1, v2, w, j in edges:
                if uf.union(v1,v2):
                    weight+=w
            if weight==mst_weight:
                pseudo.append(i)
        return [critical,pseudo]

