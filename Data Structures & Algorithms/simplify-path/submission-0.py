class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stk = []
        print(path)
        for tok in path:
            if tok == "..":
                if stk: stk.pop()
            elif tok==".":
                continue
            elif tok!="":
                stk.append(tok)
        if len(stk)==0:
            return "/"
        else:
            ans = []
            for tok in stk:
                ans.append("/"+tok)
            return "".join(ans)
