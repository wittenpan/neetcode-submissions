class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        coins.sort()
        def dfs(i,total):
            if (i, total) in memo:
                return memo[(i,total)]
            if total==amount:
                return 1
            if i>=len(coins):
                return 0
            res = dfs(i+1, total)
            if total+coins[i]<=amount:
                res += dfs(i, total+coins[i])
            memo[(i,total)] = res
            return res
        return dfs(0,0)
