class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        res = []
        line_words = self.separate(words, maxWidth)
        for i in xrange(len(line_words) - 1):
            res.append(self.join(line_words[i], maxWidth))
        
        # deal with the last line
        str = ''
        if line_words[-1]:
            str = line_words[-1][0]
            for i in xrange(1, len(line_words[-1])):
                str += ' ' + line_words[-1][i]
        
        str += ' ' * (maxWidth - len(str))
        res.append(str)
        
        return res
        
    '''
    A method to separate the words into different list, each list forms a line
    @rtype: List[List[word]]
    '''
    def separate(self, words, maxWidth):
        res = []
        path = []
        size = 0
        
        for word in words:
            if not word:
                continue
            
            if not path or size + 1 + len(word) <= maxWidth:
                size += len(word) if not path else len(word) + 1
                path.append(word)
            else:
                res.append(list(path))
                path = [word]
                size = len(word)
                
        res.append(path)
        
        return res
        
    '''
    A method to join a list of words into a line
    @rtype: string
    '''
    def join(self, words, maxWidth):
        count = len(words)
        
        # when count equals 1
        if count == 1:
            space = ''
            space += ' ' * (maxWidth - len(words[0]))
            return words[0] + space
        
        # get the total length of words
        size = 0
        for word in words:
            size += len(word)
        
        spaces = [''] * (count - 1)
        spaces_sum = maxWidth - size    # the length of spaces
        for i in xrange(spaces_sum):
            index = i % (count - 1)
            spaces[index] += ' '
        
        res = ''
        for i in xrange(count - 1):
            res += words[i]
            res += spaces[i]
            
        res += words[-1]
        return res
        

        
        
        
        