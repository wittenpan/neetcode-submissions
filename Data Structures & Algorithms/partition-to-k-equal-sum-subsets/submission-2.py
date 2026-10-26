class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k:
            return False
        nums.sort(reverse=True)
        goal = total//k
        if nums[0]>goal:
            return False
        n = len(nums)
        #mask = (1<<n)
        memo = {}
        def dfs(mask, formed, currsum):
            if mask in memo:
                return memo[mask]
            if formed==k-1:
                memo[mask] = True
                return True
            memo[mask] = False
            for i in range(len(nums)):
                if not mask & (1<<i) and nums[i]+currsum<=goal:
                    if nums[i]+currsum==goal:
                        memo[mask] |= dfs(mask |(1<<i), formed+1, 0)
                    else:
                        memo[mask] |= dfs(mask | (1<<i), formed, currsum+nums[i])
            return memo[mask]
        return dfs(0, 0, 0)
            