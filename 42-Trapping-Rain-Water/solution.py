class Solution(object):
    def trap(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if heights is None or not heights:
            return 0
            
        # get the max_left from beginning for each position
        max_left = [0]
        for i in xrange(1, len(heights)):
            max_left.append(max(max_left[-1], heights[i - 1]))
        
        # get the max_right from the tail for each position
        max_right = [0]
        for i in reversed(xrange(len(heights) - 1)):
            max_right.insert(0, max(max_right[0], heights[i + 1]))

        # get water volume
        res = 0
        for i in range(len(heights)):
            min_height = min(max_left[i], max_right[i])
            res += min_height - heights[i] if min_height > heights[i] else 0
        
        return res