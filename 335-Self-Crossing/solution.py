class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        
        if len(x) < 4:
            return False
            
        if x[2] <= x[0]:
            return self.isShrinkCrossing(3, x)
        else:
            return self.isExpandCrossing(3, x)
        
    
    def isShrinkCrossing(self, start, x):
        for i in xrange(start, len(x)):
            if x[i] >= x[i - 2]:
                return True
        
        return False
        
    def isExpandCrossing(self, start, x):
        for i in xrange(start, len(x)):
            if x[i] > x[i - 2]:     # still expanding
                continue
            
            else:   # enter shrinking mode
                if i + 1 == len(x):
                    return False
                
                bar = x[i - 4] if i - 4 >= 0 else 0
                if x[i] >= x[i - 2] - bar:
                    
                    if i + 1 < len(x) and x[i + 1] >= x[i - 1]- x[i - 3]:
                        return True
                        
                    return self.isShrinkCrossing(i + 2, x)
                
                else:
                    return self.isShrinkCrossing(i + 1, x)
                    
        return False