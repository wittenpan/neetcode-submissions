class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        #condition: if mid<target: insertion is to right of mid
        #conditon if mid>target: insertion to left of target
        insertion = 0
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
                insertion = mid+1
            else:
                r = mid-1
        return insertion

