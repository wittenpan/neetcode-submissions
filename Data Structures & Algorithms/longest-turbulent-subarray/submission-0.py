class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #you could dp[i] where dp[i] = longest turbulet from there
        #each step 2, we can choose to include or start from next
        #
        #version of kadanes
        if not arr:
            return 0
        up, down, best = 1,1,1
        for i in range(1, len(arr)):
            if arr[i]>arr[i-1]:
                up, down = down+1, 1
            elif arr[i]<arr[i-1]:
                up, down = 1, up+1
            else:
                up, down = 1, 1
            best = max(best, up, down)
        return best
