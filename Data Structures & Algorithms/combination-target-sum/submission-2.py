class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, path, currsum):
            if currsum==target:
                res.append(path.copy())
                return
            if i==len(nums) or currsum>target:
                return
            path.append(nums[i])
            backtrack(i,path,currsum+nums[i])
            path.pop()
            backtrack(i+1,path,currsum)
            
        backtrack(0,[],0)
        return res