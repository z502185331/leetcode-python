class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if len(A[0]) != len(B):
            return []
        
        m, n = len(A), len(B[0])
        
        res = [[0] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                res[i][j] = self.eval(A, B, i, j)
        return res
    
    
    def eval(self, A, B, x, y):
        res = 0
        for i in xrange(len(A[0])):
            res += A[x][i] * B[i][y]
        return res