class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in xrange(m + 1)]
        dp[0][0] = True
        
        # when s1 is empty
        for i in xrange(n):
            if s2[i] == s3[i]:
                dp[0][i + 1] = True
            else:
                break
        
        # when s2 is empty
        for i in xrange(m):
            if s1[i] == s3[i]:
                dp[i + 1][0] = True
            else:
                break
    
        for i in xrange(m):
            for j in xrange(n):
                if s3[i + j + 1] == s1[i] and s3[i + j + 1] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j + 1] or dp[i + 1][j]
                
                elif s3[i + j + 1] == s1[i]:
                    dp[i + 1][j + 1] = dp[i][j + 1]
                
                elif s3[i + j + 1] == s2[j]:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        
        return dp[m][n]