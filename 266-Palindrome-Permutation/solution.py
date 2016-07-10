class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if not s:
            return False
        
        m = len(s)
        
        # count the character
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        canOdd = ((m & 1) == 1)
        for key, val in counts.items():
            if (val & 1) == 1:
                if canOdd:
                    canOdd = False
                else:
                    return False
        
        return True