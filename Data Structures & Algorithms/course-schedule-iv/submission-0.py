class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #we want some kind of labeling, dsu maybe...?
        #we create prerequisite map; coursenum->prereqs.
        #perfect for toplogical sort, we start with indegree 0s, then build onto solution as each previous course is a prereq for the next
        #start with one indegree 0?
        q = deque()
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        prereqs = [set() for _ in range(numCourses)]
        for u,v in prerequisites:
            indegree[v]+=1
            adj[u].append(v)
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            node = q.popleft()
            for nei in adj[node]:
                prereqs[nei].add(node)
                prereqs[nei]|=prereqs[node]
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        print(prereqs)
        res = []
        for u, v in queries:
            res.append(u in prereqs[v])
        return res
