class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        
        for i in xrange(1, n):
            dp[i] = dp[i - 1] + grid[0][i]
        
        for i in xrange(1, m):
            dp[0] += grid[i][0]
            for j in xrange(1, n):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        
        return dp[n - 1]