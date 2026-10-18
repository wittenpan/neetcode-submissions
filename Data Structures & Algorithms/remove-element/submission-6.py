class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #create two pointers, one at start and one at end. 
        replacePtr = len(nums)-1
        while replacePtr>=0 and nums[replacePtr]==val:
            replacePtr-=1
        startPtr = 0
        while startPtr<=replacePtr:
            if nums[startPtr]==val:
                nums[startPtr], nums[replacePtr] = nums[replacePtr], nums[startPtr]
                replacePtr-=1
            else:
                startPtr+=1
        return replacePtr+1