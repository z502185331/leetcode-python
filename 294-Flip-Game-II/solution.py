class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if not s:
            return False
        
        for i in xrange(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+' and not self.canWin(s[: i] + '--' + s[i + 2 :]):
                return True
        return False
    
    def dfs(self, l):
        """
        @param l: the list of character in s
        @param flag: true the current player is Me
                     flase the current player is not Me
        """
        
        isWin = False
        for i in xrange(len(l) - 1):
            if l[i] == '+' and l[i + 1] == '+':
                l[i] = l[i + 1] = '-'
                isWin |= not self.dfs(l)  # When the opposite cannot win, I can win
                l[i] = l[i + 1] = '+'
        
        return isWin
                
                
                