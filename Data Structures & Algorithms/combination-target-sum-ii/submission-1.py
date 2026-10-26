class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, path, currsum):
            if currsum==target:
                res.append(path.copy())
                return
            if i==len(nums) or currsum>target:
                return
            path.append(nums[i])
            backtrack(i+1,path,currsum+nums[i])
            path.pop()
            while i+1<len(nums) and nums[i+1]==nums[i]:
                i+=1
            backtrack(i+1,path,currsum)
            
        backtrack(0,[],0)
        return res