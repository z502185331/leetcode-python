class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        if not words:
            return 0
        
        pairs = {}
        for word in words:
            pairs[word] = self.transform(word)
        
        # two words don't have common character means that pairs[word1] & pairs[word2] == 0
        max_product = 0
        # for i, word1 in enumerate(words):
        #     for j in xrange(i + 1, len(words)):
        #         word2 = words[j]
        #         if pairs[word1] & pairs[word2] == 0:
        #             max_product = max(len(word1) * len(word2), max_product)
        words.sort(cmp = lambda a, b : len(b) - len(a))
        for i in xrange(1, len(words)):
            for j in xrange(i):
                if pairs[words[i]] & pairs[words[j]] != 0:
                    continue
                
                product = len(words[i]) * len(words[j])
                if product > max_product:
                    max_product = product
                else:
                    break
        
        return max_product
    
    '''
    A method to transform word into a binary number.
    For example, 'abc' => 111(2)
    '''
    def transform(self, word):
        res = 0
        for c in word:
            res |= 1 << (ord(c) - ord('a'))
        return res