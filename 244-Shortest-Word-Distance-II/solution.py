class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        
        self.indexes = {}
        
        # get the index of word in words
        for i, word in enumerate(words):
            self.indexes[word] = self.indexes.get(word, []) + [i]

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        index1 = self.indexes[word1]
        index2 = self.indexes[word2]
        
        # find the minimum distance between two lists
        index = []
        for i in index1:
            index.append((i, 1))
        for i in index2:
            index.append((i, 2))
        
        index.sort()
        
        prev, cur = 0, 1
        distance = sys.maxint
        while cur < len(index):
            if index[cur][1] != index[prev][1]:
                distance = min(distance, index[cur][0] - index[prev][0])
            
            prev = cur
            cur += 1
        
        return distance
        
        


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")