class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total%4:
            return False
        goal = total//4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > goal:
            return False
        visited = [False] * len(matchsticks)
        def backtrack(currsum, formed):
            if formed == 3:
                return True
            if currsum == goal:
                return backtrack(0, formed+1)
            for i in range(len(matchsticks)):
                if not visited[i] and currsum+matchsticks[i]<=goal:
                    visited[i] = True
                    if backtrack(currsum+matchsticks[i], formed):
                        return True
                    visited[i] = False
            return False
        return backtrack(0, 0)