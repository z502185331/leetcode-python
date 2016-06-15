class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
            
        s = s.lower()
        alps = 'abcdefghijklmnopqrstuvwxyz0123456789'
        
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l] not in alps:
                l += 1
            
            while l < r and s[r] not in alps:
                r -= 1
            
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
            
        return True