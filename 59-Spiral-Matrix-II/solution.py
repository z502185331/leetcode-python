class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        if not n:
            return []
            
        res = [[0] * n for i in range(n)]
        c = 1
        
        for i in xrange((n + 1) / 2):
            for j in xrange(i, n - i):
                res[i][j] = c
                c += 1
            
            for j in xrange(i + 1, n - i):
                res[j][n - i - 1] = c
                c += 1
            
            if n - i - 1 != i: # when there is only one line left
                for j in reversed(xrange(i, n - i - 1)):
                    res[n - i - 1][j] = c
                    c += 1
            
            if n - i - 1 != i: # when there is only one vertical line left
                for j in reversed(xrange(i + 1, n - i - 1)):
                    res[j][i] = c
                    c += 1
        return res