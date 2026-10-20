class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)<2):
            return False
        stk = []
        dic = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char=='(' or char =='{' or char=='[':
                stk.append(char)
                print(stk)
            else:
                if len(stk)==0 or dic[stk.pop()]!=char:
                    return False
        return True if len(stk)==0 else False