class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        
        m = len(ratings)
        lefts = [1] * m
        rights = [1] * m
        
        for i in xrange(1, m):
            if ratings[i] > ratings[i - 1]:
                lefts[i] = lefts[i - 1] + 1
        
        for i in reversed(xrange(m - 1)):
            if ratings[i] > ratings[i + 1]:
                rights[i] = rights[i + 1] + 1
            
        
        count = 0
        for i in xrange(m):
            count += max(lefts[i], rights[i])
        
        return count