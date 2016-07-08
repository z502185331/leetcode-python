class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
    
        if not image or not image[0]:
            return 0
        
        m, n = len(image), len(image[0])
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = [(x, y)]
        marks = [[False] * n for _ in xrange(m)]
        min_x, max_x, min_y, max_y = m, 0, n, 0
        
        while queue:
            size = len(queue)
            for _ in xrange(size):
                cur_x, cur_y = queue.pop(0)
                min_x = min(min_x, cur_x)
                max_x = max(max_x, cur_x)
                min_y = min(min_y, cur_y)
                max_y = max(max_y, cur_y)
                marks[cur_x][cur_y] = True
                
                for offset in offsets:
                    next_x = cur_x + offset[0]
                    next_y = cur_y + offset[1]
                    
                    if 0 <= next_x < m and 0 <= next_y < n and \
                            not marks[next_x][next_y] and image[next_x][next_y] == '1':
                        queue.append((next_x, next_y))
                        
        return (max_x - min_x + 1) * (max_y - min_y + 1)
                    
            
        
    
    """
    Find the coordinates of points between (x, y), (x1, y1) is first black
    """
    def findBoundary(self, image, x, y, x1, y1):
        while x != x1 or y != y1:
            mid_x = x + (x1 - x) / 2
            mid_y = y + (y1 - y) / 2
            
            if image[mid_x][mid_y] == "1":
                if x != x1:     # vertical
                    x = mid_x
                else:           # horizontal
                    y = mid_y
            
            else:
                if x != x1:
                    x1 = mid_x + (1 if x1 < x else -1)
                else:
                    y1 = mid_y + (1 if y1 < y else -1)
        
        return x, y
                    
        