class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        
        res = [0] * length
        for update in updates:
            res[update[1]] += update[2]
            if update[0] > 0:
                res[update[0] - 1] -= update[2]
        
        s = 0
        for i in reversed(xrange(length)):
            s += res[i]
            res[i] = s
        
        return res
            