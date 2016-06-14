# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        
        if not points:
            return 0

        maxP = 1
        for point in points:
            counts = {} # record how many points on a line 
            verti_count = 0  # the vertical line cannot represent by k
            same_count = 1
            
            for other_point in points:
                if other_point is point:
                    continue
                
                if other_point.x == point.x:
                    if other_point.y == point.y: # same point
                        same_count += 1
                    else:
                        verti_count += 1    # same vertical line
                else:
                    k = (other_point.y - point.y) / float(other_point.x - point.x)
                    counts[k] = counts.get(k, 0) + 1

            # compare the max points on the line
            max_local = verti_count
            if counts.values():
                max_local = max(max(counts.values()), max_local)
            max_local += same_count
            
            maxP = max(max_local, maxP)
        return maxP