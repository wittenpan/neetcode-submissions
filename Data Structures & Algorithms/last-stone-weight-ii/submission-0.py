class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones.sort()
        #equal to partitioning between two groups and finding min diff 
        su = sum(stones)
        target = (su+1)//2
        memo = {}
        def dfs(i, total):
            if (i,total) in memo:
                return memo[((i,total))]
            if total>=target or i==len(stones):
                return abs(total-(su-total))
            memo[(i,total)] = min(dfs(i+1,total), dfs(i+1,total+stones[i]))
            return memo[(i,total)]
        return dfs(0,0)