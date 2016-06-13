class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        d = {}
        for i in xrange(len(s)):
            cs = s[i]
            ct = t[i]
            
            if cs in d:
                if d[cs] != ct:
                    return False
            else:
                if ct in d.values():
                    return False
                d[cs] = ct
        
        return True
            
            
        
        