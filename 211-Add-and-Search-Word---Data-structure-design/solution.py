class TrieNode(object):
    def __init__(self):
        self.word = None
        self.children = [None] * 26
        
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        
        def add_helper(node, index):
            if index == len(word):
                node.word = word
                return
            
            c = word[index]
            i = ord(c) - ord('a')
            if node.children[i] is None:
                node.children[i] = TrieNode()
            
            add_helper(node.children[i], index + 1)
        
        add_helper(self.root, 0)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        def search_helper(node, index):
            if index == len(word):
                return node.word is not None
            
            c = word[index]
            
            if c == '.':
                for child in node.children:
                    if child is not None:
                        if search_helper(child, index + 1):
                            return True
                            
                return False
                
            else:
                i = ord(c) - ord('a')
                if node.children[i] is None:
                    return False
            
                return search_helper(node.children[i], index + 1)
            
        return search_helper(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")