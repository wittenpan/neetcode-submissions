class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        #sort, then its optimal to take from left and right
        l, r = 0, len(people)-1
        ans = 0
        print(people)
        while l<=r:
            while people[l]+people[r]>limit and l<r:
                ans+=1
                r-=1
            ans+=1
            l+=1
            r-=1
        return ans