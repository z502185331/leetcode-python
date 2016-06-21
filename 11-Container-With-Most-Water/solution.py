class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if not height:
            return 0
        
        m = len(height)
        l, r = 0, m - 1
        
        max_vol = 0
        while l < r:
            max_vol = max(max_vol, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_vol