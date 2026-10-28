class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #generate a topological sort
        #find first letter where they differ that means a<b
        #first verify if is valid and generate adj list
        adj = defaultdict(list) # letter -> next letter
        indegree = defaultdict(int)
        for word in words:
            for c in word:
                indegree[c] = 0
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                #invalidate possible if all letters w1 == w2 and w2 runs out
                if j==len(w2):
                    return ""
                if w1[j]!=w2[j]:
                    indegree[w2[j]]+=1
                    adj[w1[j]].append(w2[j])
                    break
        res = []
        q = deque()
        for char, indeg in indegree.items():
            if indeg==0:
                q.append(char)
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return "".join(res) if len(res)==len(indegree) else ""



                
