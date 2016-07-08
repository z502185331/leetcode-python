class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        
        return self.sol_binarySearch(image, x, y)
        
    def sol_binarySearch(self, image, x, y):
        if not image or not image[0]:
            return 0

        m, n = len(image), len(image[0])
        min_col = self.binarySearch(image, -1, y, 0, m - 1, True, True)
        max_col = self.binarySearch(image, y, n, 0, m - 1, True, False)
        min_row = self.binarySearch(image, -1, x, min_col, max_col, False, True)
        max_row = self.binarySearch(image, x, m, min_col, max_col, False, False)

        return (max_row - min_row + 1) * (max_col - min_col + 1)

    """
    Find the boundary
    """
    def binarySearch(self, image, lower, upper, minimum, maximum, isVerti, goLower):
        while lower + 1 < upper:
            mid = lower + (upper - lower) / 2
            isFound = False

            for i in xrange(minimum, maximum + 1):  # find whether there is black pixel in range
                if (image[i][mid] if isVerti else image[mid][i]) == '1':
                    isFound = True
                    break

            if isFound == goLower:
                upper = mid
            else:
                lower = mid

        return upper if goLower else lower
    
    
    def sol_bfs(self, image, x, y):
        if not image or not image[0]:
            return 0
        
        m, n = len(image), len(image[0])
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = [(x, y)]
        marks = {(x, y)}
        min_x, max_x, min_y, max_y = m, 0, n, 0
        
        while queue:
            cur_x, cur_y = queue.pop(0)
            min_x = min(min_x, cur_x)
            max_x = max(max_x, cur_x)
            min_y = min(min_y, cur_y)
            max_y = max(max_y, cur_y)
            
            
            for offset in offsets:
                next_x = cur_x + offset[0]
                next_y = cur_y + offset[1]
                
                if 0 <= next_x < m and 0 <= next_y < n and \
                        (next_x, next_y) not in marks and image[next_x][next_y] == '1':
                    marks |= {(next_x, next_y)}
                    queue.append((next_x, next_y))
                        
        return (max_x - min_x + 1) * (max_y - min_y + 1)

            
        
    
    
                    
        