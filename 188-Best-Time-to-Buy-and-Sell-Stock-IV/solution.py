class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or not k:
            return 0
        
        if k > len(prices):
            return self.maxProfit1(prices)
        
        m = len(prices)
        local_dp = [0] * (k + 1)
        global_dp = [0] * (k + 1)
        
        for i in xrange(m - 1):
            diff = prices[i + 1] - prices[i]
            for j in reversed(xrange(1, k + 1)):
                local_dp[j] = max(global_dp[j - 1] + max(diff, 0), \
                        local_dp[j] + diff) 
                global_dp[j] = max(global_dp[j], local_dp[j])
    
        return global_dp[-1]
        
        
    def maxProfit1(self, prices):
        res = 0
        for i in xrange(len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                res += prices[i + 1] - prices[i]
        return res