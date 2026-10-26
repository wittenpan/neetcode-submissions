class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #need to keep balance. have to have +pos or 0 balance with +1 denoting open paren
        res = []
        def backtrack(path, o, c):
            nonlocal res
            balance = o-c
            if balance==0 and len(path)==n*2:
                res.append("".join(path))
                return
            if c>n or o>n:
                return
            if balance>0:
                path.append(")")
                backtrack(path, o, c+1)
                path.pop()
            path.append("(")
            backtrack(path, o+1, c)
            path.pop()
        backtrack([],0,0)
        return res