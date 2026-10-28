class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, node):
        curr = node
        while curr!=self.parent[node]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu==pv: return False
        if self.rank[pu]>self.rank[pv]:
            pu,pv = pv, pu
        self.parent[pu] = pv
        self.rank[pv]+=self.rank[pu]
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        #treat as connected components
        #we can union find? and n^2 loop checking if not self.find?
        #n^2 tle brute force
        n = len(nums)
        uf = DSU(n)
        if n==1: return True
        if 1 in nums:
            return False
        seen = {} #prime factor -> first index containing it
        for i, num in enumerate(nums):
            d = 2
            while d * d <= num:
                if num % d == 0:
                    if d in seen:
                        uf.union(i, seen[d])
                    else:
                        seen[d] = i
                    while num%d == 0:
                        num//= d
                d+=1
            #remaining prime factor
            if num>1:
                if num in seen:
                    uf.union(i, seen[num])
                else:
                    seen[num] = i
        return len(set(uf.find(i) for i in range(n)))==1