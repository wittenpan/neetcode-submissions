class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        potential_len = min([len(s) for s in strs])
        
        for i in range(potential_len):
            candidate = strs[0][i]
            for j in range(len(strs)):
                if candidate!=strs[j][i]:
                    return ans
            ans+=candidate
        return ans
            