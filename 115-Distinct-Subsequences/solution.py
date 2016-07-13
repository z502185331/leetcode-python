class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in xrange(m + 1)]
        
        for i in xrange(m + 1):
            dp[i][0] = 1    # when t is empty, there are only one way to delete char
        
        for i in xrange(m):
            for j in xrange(n):
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
        
        return dp[m][n]
                