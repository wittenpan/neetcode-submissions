class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f, t, tw = 0,0,0
        for bill in bills:
            if bill == 5:
                f+=1
            elif bill == 10:
                t+=1
                f-=1
                if f<0:
                    return False
            #optimal to use 10s first, because 10s cant be used for anything else
            else:
                if t>=1:
                    t-=1
                    f-=1
                else:
                    f-=3
                if f<0:
                    return False
        return True


        