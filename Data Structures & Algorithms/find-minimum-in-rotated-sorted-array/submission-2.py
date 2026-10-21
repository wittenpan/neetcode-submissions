class Solution:
    def findMin(self, nums: List[int]) -> int:
        #min is when mid>mid+1
        l, r = 0, len(nums)-1
        ans = nums[0]
        while l<=r:
            mid = (l+r)//2
            ans = min(ans, nums[mid])
            if nums[mid]<nums[r]:
                r = mid-1
            else: #nums[mid]>nums[r]
                l = mid+1
        return ans