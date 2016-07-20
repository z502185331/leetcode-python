class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        m = len(prices)
        buys = [0] * m      # max profit when buy on ith day
        sells = [0] * m     # max profit when sell on ith day
        res = 0
        
        buys[0] = -prices[0]
        
        for i in xrange(1, m):
            diff = prices[i] - prices[i - 1]
            
            sells[i] = max(buys[i - 1] + prices[i], sells[i - 1] + diff)
            buys[i] = max(sells[i - 2] - prices[i], buys[i - 1] - diff) if i >= 2 else buys[i - 1] - diff
            
            res = max(res, sells[i])
        
        return res