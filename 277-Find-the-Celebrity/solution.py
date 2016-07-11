# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        candidate = 0
        for i in xrange(n):
            if knows(candidate, i): # get the last person knows nobody later
                candidate = i
        
        
        for i in xrange(candidate):
            if knows(candidate, i): # check whether the candidate knows the person before him
                return -1
        
        for i in xrange(n):
            if not knows(i, candidate):
                return -1
        
        return candidate