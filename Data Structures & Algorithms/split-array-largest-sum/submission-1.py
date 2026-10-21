class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #can bs over answer space and greedily check like koko and min days to ship
        def canSplit(mSum):
            currSum = 0
            needed_partitions = 1
            for num in nums:
                if num+currSum>mSum:
                    currSum = 0
                    needed_partitions+=1
                currSum+=num
            return needed_partitions<=k
        l, r = max(nums), sum(nums)
        ans = float('inf')
        while l<=r:
            mid = (l+r)//2
            if canSplit(mid):
                ans = min(mid,ans)
                r = mid-1
            else:
                l = mid+1
        return ans

