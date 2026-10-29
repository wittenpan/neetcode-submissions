class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        def dfs(num):
            if num in dp:
                return dp[num]
            dp[num] = 0 if num==n else num
            for i in range(1,num):
                val = dfs(i)*dfs(num-i)
                dp[num] = max(val, dp[num])
            return dp[num]
        return dfs(n)
