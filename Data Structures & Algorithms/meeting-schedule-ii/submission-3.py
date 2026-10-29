"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = defaultdict(int)
        for interval in intervals:
            start, end = interval.start, interval.end
            events[start]+=1
            events[end]-=1
        currMeetings = 0
        res = 0
        for event in sorted(events):
            currMeetings+=events[event]
            res = max(res, currMeetings)
        return res