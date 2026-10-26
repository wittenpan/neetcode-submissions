class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(path, selected):
            nonlocal res
            if len(path)==len(selected):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if i and nums[i]==nums[i-1] and not selected[i-1]:
                    continue
                if not selected[i]:
                    selected[i] = True
                    path.append(nums[i])
                    backtrack(path,selected)
                    path.pop()
                    selected[i] = False
        backtrack([],[False]*len(nums))
        return res