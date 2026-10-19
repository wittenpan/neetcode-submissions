class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        runningSum = 0
        sum_to_count = {0:1}
        ans = 0
        for num in nums:
            runningSum+=num
            ans += sum_to_count.get(runningSum-k,0)
            sum_to_count[runningSum] = sum_to_count.get(runningSum,0)+1
        return ans