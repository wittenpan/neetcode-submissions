class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i>=len(cost):
                return 0
            cache[i] = cost[i]+min(dfs(i+1),dfs(i+2))
            return cache[i]
        return min(dfs(0),dfs(1))
