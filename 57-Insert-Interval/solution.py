# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        if not intervals:
            return [newInterval]
        
        l = []
        for i in intervals:
            if newInterval.end < i.start:
                l.append(newInterval)
                newInterval = i
                
            elif newInterval.start > i.end:
                l.append(i)
            
            else:
                newInterval.start = min(i.start, newInterval.start)
                newInterval.end = max(i.end, newInterval.end)
        
        l.append(newInterval)
        return l