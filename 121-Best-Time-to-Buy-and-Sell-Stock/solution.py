class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
            
        prev_min = sys.maxint
        ans = 0
        
        for num in prices:
            ans = max(ans, num - prev_min)
            prev_min = min(prev_min, num)
        
        return ans