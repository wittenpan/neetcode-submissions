class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #keep positives in the stk, then handle collisions with larger asteroids
        stk = []
        for asteroid in asteroids:
            if asteroid>0 or (not stk and asteroid<0) or (asteroid<0 and stk[-1]<0):
                stk.append(asteroid)
            else:
                equal = False
                while stk and stk[-1]>0 and abs(stk[-1])<=abs(asteroid):
                    if abs(stk[-1])==abs(asteroid):
                        stk.pop()
                        equal = True
                        break
                    stk.pop()
                if not equal and (not stk or stk[-1]<0): stk.append(asteroid)
        return stk