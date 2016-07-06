# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
            
        timestamps = []
        for interval in intervals:
            timestamps.append((interval.start, 1))
            timestamps.append((interval.end, 0))
        
        timestamps.sort(key = lambda x : (x[0], x[1]))
        max_room = 0
        cur_room = 0
        for stamp in timestamps:
            if stamp[1] == 1:
                cur_room += 1
            else:
                cur_room -= 1
            
            max_room = max(max_room, cur_room)
        
        return max_room