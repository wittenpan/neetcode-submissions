class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we can find pivot index, then bs in each half
        pivot = 0
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if mid>0 and nums[mid]<nums[mid-1]:
                pivot = mid
                break
            if nums[mid]<nums[r]:
                #ans in left half
                r = mid-1
            else:
                l = mid+1
        l, r = 0, pivot-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        l, r = pivot, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return -1
