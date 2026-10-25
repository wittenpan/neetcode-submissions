class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #sweep line... onlogn
        events = defaultdict(int)
        for p, s, e in trips:
            if e<s:
                return False
            events[s]+=p
            events[e]-=p
        passengers = 0

        for event in sorted(events):
            passengers+=events[event]
            if passengers>capacity:
                return False
        return True