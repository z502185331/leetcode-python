class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        num = 0
        for c in s:
            num = num * 26 + (ord(c) - 64)
        return num
        