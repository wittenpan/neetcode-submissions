class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)+1
        #cant modify while iterating...
        for num in nums:
            idx = abs(num)-1
            if nums[idx]<0:
                return abs(num)
            nums[idx]*=-1
        return -1