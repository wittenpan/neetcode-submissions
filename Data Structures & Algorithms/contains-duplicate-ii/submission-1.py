class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0 or len(nums)==1:
            return False
        #keep window size of k
        seen = set()
        for i in range(k):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        l = 0
        for r in range(k, len(nums)):
            if nums[r] in seen:
                return True
            seen.remove(nums[l])
            seen.add(nums[r])
            l+=1
        return False