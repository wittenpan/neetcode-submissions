class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i>=len(stoneValue):
                return 0
            res = float('-inf')
            taken = 0
            for j in range(i,min(len(stoneValue),i+3)):
                taken+=stoneValue[j]
                res = max(res, taken-dfs(j+1))
            memo[i] = res
            return res
        ans = dfs(0)
        if ans>0:
            return "Alice"
        elif ans<0:
            return "Bob"
        else:
            return "Tie"