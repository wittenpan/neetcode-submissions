class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        #we can keep monotonic stk of (time to end), a fleet will catch up if 
        #stk[-1][0]<time to end x
        cars = sorted(zip(position, speed), reverse=True)
        for pos, spd in cars:
            time = (target-pos)/spd   
            stk.append(time)
            if len(stk)>=2 and stk[-1]<=stk[-2]:
                stk.pop()
        return len(stk)