class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
        if not envelopes:
            return 0
        
        envelopes.sort()
        m = len(envelopes)
        dp = [1] * m
        res = 1
        
        for i in xrange(1, m):
            for j in reversed(xrange(i)):
                if envelopes[i][0] == envelopes[j][0]:  # same width
                    continue
                
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
            res = max(res, dp[i])
        return res
            