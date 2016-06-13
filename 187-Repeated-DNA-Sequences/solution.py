class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        
        res = []
        history = set() # store the sequence that has been processed
        
        for i in xrange(len(s) - 9):
            cur = s[i : i + 10]
            if cur not in history:
                history.add(cur)
            else:
                if cur not in res:
                    res.append(cur)
        
        return res