class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        if not s:
            return []
        
        res = []
        for i in xrange(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                res.append(s[: i] + '--' + s[i + 2 :])
        
        return res