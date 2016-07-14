class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        if not costs:
            return 0
        
        m, k = len(costs), len(costs[0])
        dp = [[0] * k for _ in xrange(m)]
        globalMin1, globalMin2 = (0, -1), (0, -1)
        
        for i in xrange(m):
            min1, min2 = (sys.maxint, -1), (sys.maxint, -1)
            
            for j in xrange(k):
                if j == globalMin1[1]:
                    dp[i][j] = globalMin2[0] + costs[i][j]
                    
                else:
                    dp[i][j] = globalMin1[0] + costs[i][j]
                
                if dp[i][j] < min1[0]:
                    min2 = min1
                    min1 = (dp[i][j], j)
                    
                elif dp[i][j] < min2[0]:
                    min2 = (dp[i][j], j)
            
            globalMin1, globalMin2 = min1, min2
        
        return globalMin1[0]