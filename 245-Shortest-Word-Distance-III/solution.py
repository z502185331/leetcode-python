class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        if not words:
            return 0
        
        prev = (-1, None)
        distance = len(words)
        for i in xrange(len(words)):
            if words[i] in {word1, word2}:
                if prev[1] is not None and (prev[1] != words[i] or word1 == word2):
                    distance = min(distance, i - prev[0])
                
                prev = (i, words[i])
        
        return distance