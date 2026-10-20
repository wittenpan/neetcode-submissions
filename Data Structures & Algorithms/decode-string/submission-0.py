class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        num = 0
        i = 0
        while i<len(s):
            if s[i].isnumeric():
                num = 0
                while i<len(s) and s[i].isnumeric():
                    num = num*10+int(s[i])
                    i+=1
                stk.append(num)
                #skip [
                i+=1
            elif s[i]=="]":
                sb = ""
                while stk and isinstance(stk[-1],str):
                    sb = stk.pop()+sb
                stk.append(stk.pop()*sb)
                i+=1
            else:
                stk.append(s[i])
                i+=1
        return "".join(stk)