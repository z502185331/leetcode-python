class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        return self.sol_dp(coins, amount)
    
    
    # TLE
    def dfs(self, coins, amount, length):
        if amount == 0:
            return length
        
        res = sys.maxint
        for coin in coins:
            if coin > amount:
                continue
            
            local = self.dfs(coins, amount - coin, length + 1)
            if local != -1:
                res = min(res, local)
                
        return res if res != sys.maxint else -1
        
    
    # TLE
    def sol_dp(self, coins, amount):
        m = len(coins)
        dp = [sys.maxint] * (amount + 1)
        dp[0] = 0
        
        # for i in xrange(1, amount + 1):
        #     for j in xrange(m):
        #         if i < coins[j]:
        #             continue
            
        #         dp[i] = min(dp[i], dp[i - coins[j]] + 1)
            
        # return dp[-1] if dp[-1] != sys.maxint - 1 else -1
        
        for coin in coins:
            for i in xrange(coin, amount + 1):
                if dp[i - coin] != sys.maxint:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != sys.maxint else -1
        
        
    
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
        