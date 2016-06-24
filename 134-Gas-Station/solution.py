class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        if not gas or not cost:
            return -1
        
        m = len(gas)
        total_gas = 0
        cur_gas = 0
        start_index = 0
        
        for i in xrange(m):
            total_gas += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]
            
            # not enough gas
            if cur_gas < 0:
                cur_gas = 0
                start_index = i + 1
        
        return start_index if total_gas >= 0 else -1
        
        