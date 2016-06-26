class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        max_area = 0
        
        dp = [[0] * (n + 1) for i in xrange(m + 1)]
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == '0':
                    continue
                
                dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                max_area = max(max_area, dp[i + 1][j + 1] * dp[i + 1][j + 1])
        
        return max_area