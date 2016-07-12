class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        m = len(coins)
        dp = [sys.maxint - 1] * (amount + 1)
        dp[0] = 0
        
        for i in xrange(1, amount + 1):
            for j in xrange(m):
                if i < coins[j]:
                    continue
            
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
            
        return dp[-1] if dp[-1] != sys.maxint - 1 else -1
                
        
        
    
    # TLE
    def sol_bfs(self, coins, amount):
        count = 0
        queue = [amount]
        
        while queue:
            size = len(queue)
            for _ in xrange(size):
                target = queue.pop(0)
                
                if target == 0:
                    return count
                
                for coin in coins:
                    if target - coin < 0:   # beyond the target amount
                        continue
                    
                    
                    queue.append(target - coin)
            count += 1
        
        return -1
        