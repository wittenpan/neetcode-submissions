class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        ct = 1
        for i in range(1, len(nums)):
            if nums[i]==candidate:
                ct+=1
            elif nums[i]!=candidate:
                ct-=1
                if ct==0:
                    candidate = nums[i]
                    ct = 1
        return candidate