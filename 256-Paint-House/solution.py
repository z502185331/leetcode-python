class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        if not costs:
            return 0
        
        m = len(costs)
        dp = [[0] * 3 for _ in xrange(m + 1)]
        
        for i in xrange(m):
            for j in xrange(3):
                dp[i + 1][j] = costs[i][j]
                
                # add the minimum cost of painting i - 1 house with different color
                if j == 0:
                    dp[i + 1][j] += min(dp[i][1], dp[i][2])
                elif j == 1:
                    dp[i + 1][j] += min(dp[i][0], dp[i][2])
                else:
                    dp[i + 1][j] += min(dp[i][0], dp[i][1])
                    
        return min(dp[m])