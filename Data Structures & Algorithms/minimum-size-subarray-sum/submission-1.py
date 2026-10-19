class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum = 0
        l = 0
        ans = float('inf')
        for r in range(len(nums)):
            currSum+=nums[r]
            while currSum>=target:
                ans = min(ans, r-l+1)
                currSum-=nums[l]
                l+=1
                
        return ans if ans!=float('inf') else 0
            