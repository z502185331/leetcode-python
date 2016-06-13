class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        
        res = []
        for i in xrange(len(s) - 9):
            cur = s[i : i + 10]
            if s.count(cur) > 1 and cur not in res:
                res.append(cur)
        
        return res