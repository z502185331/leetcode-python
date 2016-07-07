class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.matrix = [[1,2,3], [4,5,6], [7,8,9]]
        self.offsets = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), 
                        (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        
        count = 0
        for i in xrange(3):
            for j in xrange(3):
                count += self.dfs(m, n, i, j, [self.matrix[i][j]])
        return count
    
    def dfs(self, m, n, x, y, path):
        count = 0
        if m <= len(path) < n: # the path itself is a valid pattern
            count += 1
            
        elif len(path) == n:
            return 1

        for offset in self.offsets:
            new_x = x + offset[0]
            new_y = y + offset[1]
            
            while 0 <= new_x < 3 and 0 <= new_y < 3 and \
                    self.matrix[new_x][new_y] in path:
                new_x += offset[0]
                new_y += offset[1]
            
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                path.append(self.matrix[new_x][new_y])
                count += self.dfs(m, n, new_x, new_y, path)
                path.pop()
                
        return count  
