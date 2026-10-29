class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, holding):
            if (i,holding) in memo:
                return memo[(i,holding)]
            if i>=len(prices):
                return 0
            res = 0
            if not holding:
                res = max(res, dfs(i+1, True) - prices[i],dfs(i+1, False))
            else:
                res = max(res, dfs(i+2, False) + prices[i], dfs(i+1, True))
            memo[(i,holding)] = res
            return res
        return dfs(0, False)