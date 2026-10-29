class Solution:
    def numSquares(self, n: int) -> int:
        #knapsack again, n=10,000
        squares = [i**2 for i in range(101)]
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for square in squares:
                if i-square>=0:
                    dp[i] = min(dp[i-square]+1,dp[i])
        return dp[-1]