class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix or not matrix[0]:
            return []
            
        m = len(matrix)
        n = len(matrix[0])
        
        x = y = 0
        res = []
        while m > 0 and n > 0:
            if m == 1:
                for i in xrange(n):
                    res.append(matrix[x][y])
                    y += 1
                break
            
            if n == 1:
                for i in xrange(m):
                    res.append(matrix[x][y])
                    x += 1
                break
            
            for i in xrange(n - 1):
                res.append(matrix[x][y])
                y += 1
            
            for i in xrange(m - 1):
                res.append(matrix[x][y])
                x += 1
            
            for i in xrange(n - 1):
                res.append(matrix[x][y])
                y -= 1
            
            for i in xrange(m - 1):
                res.append(matrix[x][y])
                x -= 1
            
            x += 1
            y += 1
            m -= 2
            n -= 2
        
        return res
                