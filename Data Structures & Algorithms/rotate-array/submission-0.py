class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #mod n because rorating anything over n same effect
        #final position of item = (orig_i+k)%n
        n = len(nums)
        k = k%n
        #k = 2
        #[1,2,3,4,5]
        # ^       ^
        #we can approach with a cyclical placing algo
        count = 0
        start = 0
        while count<n:
            curr = start
            prev = nums[start]
            while True:
                next_idx = (curr+k)%n
                nums[next_idx], prev = prev, nums[next_idx]
                curr = next_idx
                count+=1
                if start==curr:
                    break
            start+=1
        