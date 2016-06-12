class TrieNode(object):
    def __init__(self):
        self.word = None
        self.children = {}
    
    @classmethod
    def build(cls, root, word):
        
        def helper(node, index):
            if index == len(word):
                node.word = word
                return
            
            c = word[index]
            node.children[c] = node.children.get(c, TrieNode())
            
            helper(node.children[c], index + 1)
        
        helper(root, 0)
                

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        if not words:
            return []
        
        root = TrieNode()
        for word in words:
            TrieNode.build(root, word)
        
        m = len(board)
        n = len(board[0])
        isVisit = [[False] * n for i in xrange(m)]
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        res = []
        
        def dfs(i, j, node):
            
            if node.word is not None and node.word not in res:  # find the word
                res.append(node.word)
                if not node.children:  # find the leaf node and no more word with same prefix existed
                    return
            
            isVisit[i][j] = True
            for o in offsets:
                new_i = i + o[0]
                new_j = j + o[1]
                if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and not isVisit[new_i][new_j] and \
                        board[new_i][new_j] in node.children:
                    dfs(new_i, new_j, node.children[board[new_i][new_j]])
                    isVisit[new_i][new_j] = False
            
            isVisit[i][j] = False
            
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] in root.children:
                    dfs(i, j, root.children[board[i][j]])
        
        return res
            