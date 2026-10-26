class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #judge has n-1 indegree
        candidates = []
        indegree = [0]*n
        adj = [[] for _ in range(n)]
        for u, v in trust:
            u-=1
            v-=1
            indegree[v]+=1
            adj[u].append(v)
            if indegree[v]==n-1:
                candidates.append(v)
        for candidate in candidates:
            if len(adj[candidate])==0:
                return candidate+1
        return -1
        