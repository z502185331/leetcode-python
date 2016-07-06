class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        
        res = []
        self.dfs(word, 0, res, [])
        return res
    
    def dfs(self, word, index, res, path):
        if index >= len(word):
            res.append(''.join(path))
            return
        
        for length in xrange(len(word) - index + 1):    # the length to abbr
            if length != 0:
                path.append(str(length))
            if index + length < len(word):
                path.append(word[index + length])
            
            self.dfs(word, index + length + 1, res, path)
            
            if index + length < len(word):
                path.pop()
            if length != 0:
                path.pop()