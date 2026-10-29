class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, total):
            if total==target and i==len(nums):
                return 1
            elif i==len(nums):
                return 0
            if (i,total) in memo:
                return memo[(i,total)]
            res = dfs(i+1,total-nums[i]) + dfs(i+1,total+nums[i])
            memo[(i,total)] = res
            return res
        return dfs(0,0)