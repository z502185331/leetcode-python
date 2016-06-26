class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        if not word:
            return True
        if not board:
            return False
            
        m = len(board)
        n = len(board[0])
        isVisited = [[False] * n for i in range(m)]
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        '''
        @param i,j the coordinate of char
        @param index the index of current char need to be found
        '''
        def dfs(i, j, index):
            if index == len(word):
                return True
            
            isVisited[i][j] = True
            for offset in offsets:
                new_i, new_j = i + offset[0], j + offset[1]
                if new_i >= 0 and new_i < m and \
                    new_j >= 0 and new_j < n and \
                        not isVisited[new_i][new_j] and \
                            word[index] == board[new_i][new_j]:
                    if dfs(new_i, new_j, index + 1): # find the word
                        return True
                        
                    isVisited[new_i][new_j] = False
            isVisited[i][j] = False
            
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
        
        return False