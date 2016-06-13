class TrieNode(object):
    def __init__(self):
        self.word = None
        self.children = [None for i in xrange(26)]

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        
        def insert_helper(node, index):
            if index == len(word):
                node.word = word
                return
          
            c = word[index]
            i = ord(c) - ord('a')
            if node.children[i] is None:
                node.children[i] = TrieNode()
              
            insert_helper(node.children[i], index + 1)
      
        insert_helper(self.root, 0)
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        def search_helper(node, index):
            if node is None:
                return False
              
            if index == len(word):
                return node.word is not None
          
            c = word[index]
            return search_helper(node.children[ord(c) - ord('a')], index + 1)
      
        return search_helper(self.root, 0)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        def startwith_helper(node, index):
            if node is None:
                return False
             
            if index == len(prefix):
                return True
          
            c = prefix[index]
            return startwith_helper(node.children[ord(c) - ord('a')], index + 1)
      
        return startwith_helper(self.root, 0)

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")