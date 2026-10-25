class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        def backtrack(i, curr):
            nonlocal ans
            if i==len(nums):
                ans+=curr
                return
            backtrack(i+1, curr^nums[i])
            backtrack(i+1, curr)
        backtrack(0,0)
        return ans