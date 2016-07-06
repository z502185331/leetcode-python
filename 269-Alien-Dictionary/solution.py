class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.prev = None
        
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        if not words:
            return ''
        
        # build the tree and graph
        self.graph = {}
        self.marks = {}
        root = TrieNode()
        for word in words:
            if not word:
                continue
            
            self.buildTree(root, word, 0)
        
        # BFS to traverse the level of tree
        res = []
        for node in self.graph:
            if self.marks[node] == 2:
                continue
            if not self.sort(node, res):
                return ''
                
        return ''.join(res)
        
    
    def sort(self, cur, res):
        if self.marks[cur] == 1:
            return False
        
        self.marks[cur] = 1
        for nextNode in self.graph[cur]:
            if self.marks[nextNode] == 2:
                continue
            
            if not self.sort(nextNode, res):
                return False
        
        self.marks[cur] = 2
        res.insert(0, cur)
        return True
        

    def buildTree(self, root, word, index):
        if index == len(word):
            return
        
        cur = word[index]
        if cur not in root.children:
            root.children[cur] = TrieNode()
        
        # build the graph
        if root.prev is not None and root.prev != cur:
            self.graph[root.prev] = self.graph.get(root.prev, []) + [cur]
            
        root.prev = cur
        self.graph[cur] = self.graph.get(cur, [])
        self.marks[cur] = 0
            
        self.buildTree(root.children[cur], word, index + 1)
        