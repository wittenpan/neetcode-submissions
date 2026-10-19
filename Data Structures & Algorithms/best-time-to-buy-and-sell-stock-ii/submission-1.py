class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy and sell on same day... no effect
        memo = {}
        def dfs(i, holding):
            if i==len(prices)-1:
                if holding:
                    return prices[i]
                else:
                    return 0
            if (i, holding) in memo:
                return memo[(i,holding)]
            ans = 0
            if holding:
                ans = max(ans, prices[i]+dfs(i+1, False))
            else:
                ans = max(ans, -prices[i]+dfs(i+1, True))
            ans = max(ans, dfs(i+1, holding))
            memo[(i,holding)] = ans
            return ans
        return dfs(0,False)
            