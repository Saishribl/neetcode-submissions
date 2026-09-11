"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)
        rooms = 0
        res = 0
        i = j = 0
        
        while i < len(intervals):
            if starts[i] < ends[j]:
                rooms+=1
                res = max(res, rooms)
                i+=1
            else:
                rooms-=1
                j+=1
        return res