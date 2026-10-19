class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #n^2 possible
        print(nums)
        ans = []
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            target = -nums[i]
            #l+r = -i
            while l<r:
                s = nums[l]+nums[r]
                if s==target:
                    ans.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r: l+=1
                elif s<target:
                    l+=1
                else:
                    r-=1
        return ans