# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        if not intervals:
            return []
        
        # sort the intervals by interval.start
        intervals.sort(cmp = lambda x, y : x.start - y.start)
            
        res = []
        prev = intervals[0]
        for i in xrange(1, len(intervals)):
            cur = intervals[i]
            if prev.end < cur.start:
                res.append(prev)
                prev = cur
            elif prev.start > cur.end:
                res.append(cur)
            else:
                prev.start = min(prev.start, cur.start)
                prev.end = max(prev.end, cur.end)
        
        res.append(prev)
        return res