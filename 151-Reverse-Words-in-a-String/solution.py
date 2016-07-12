import re
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:
            return s
        
        s = re.sub('\s+', ' ', s).strip() 
        s = self.reverse(s, 0, len(s) - 1)
        l = 0
        
        while l < len(s):
            if s[l] != ' ':
                r = l + 1
                while r < len(s) and s[r] != ' ':
                    r += 1
                
                s = self.reverse(s, l, r - 1)
                
                l = r
                
            l += 1
            
        return s
        
        
        
    def reverse(self, s, start, end):
        return s[: start] + s[start : end + 1][:: -1] + s[end + 1 :]