class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = DSU(len(accounts))
        #email to index of acc
        emailToAccount = {}
        for i, a in enumerate(accounts):
            #emails
            for e in a[1:]:
                if e in emailToAccount:
                    uf.union(i, emailToAccount[e])
                else:
                    emailToAccount[e] = i
        emailGroups = defaultdict(list)
        for e, i in emailToAccount.items():
            lead = uf.find(i)
            emailGroups[lead].append(e)
        res = []
        for i, emails in emailGroups.items():
            res.append([accounts[i][0]]+sorted(emailGroups[i]))
        return res