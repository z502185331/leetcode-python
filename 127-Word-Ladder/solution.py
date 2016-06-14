class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        
        if beginWord == endWord or not wordList:
            return 0
        
        wordList.add(beginWord)
        wordList.add(endWord)
        self.source = 'abcdefghijklmnopqrstuvwxyz'
        
        queue = [beginWord]
        s = set()
        count = 1
        
        while queue:
            size = len(queue)
            count += 1
            for i in xrange(size):
                word = queue.pop(0)
                l = self.nextWords(word, wordList)
                
                for next_word in l:
                    if next_word == endWord:
                        return count
                    
                    if next_word in s:
                        continue
                    
                    s.add(next_word)
                    queue.append(next_word)
        return 0
        
        
        
    
    def nextWords(self, word, wordList):
        l = []
        for i in xrange(len(word)):
            for c in self.source:
                next_word = word[: i] + c + word[i + 1 :]
                if c == word:
                    continue
                
                if next_word in wordList:
                    l.append(next_word)
        return l
                
        
        