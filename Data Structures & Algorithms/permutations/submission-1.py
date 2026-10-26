class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, selected):
            nonlocal res
            if len(path)==len(selected):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not selected[i]:
                    selected[i] = True
                    path.append(nums[i])
                    backtrack(path,selected)
                    path.pop()
                    selected[i] = False
        backtrack([],[False]*len(nums))
        return res