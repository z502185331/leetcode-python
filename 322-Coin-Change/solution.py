class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
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
        