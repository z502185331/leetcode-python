class UnionFind(object):
    def __init__(self, len):
        self.sets = [i for i in xrange(len)]
    
    def union(self, offset1, offset2):
        if self.sets[offset1] == self.sets[offset2]:
            return
        
        self.sets[offset2] = self.sets[offset1]
    
    def find(self, offset):
        while offset != self.sets[offset]:
            tmp = self.sets[offset]
            self.sets[offset] = self.sets[self.sets[offset]]
            offset = tmp
        
        return self.sets[offset]
            

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        self.sol_unionFind(board)
    
    
    def sol_unionFind(self, board):
        if board is None or not board:
            return
        
        m = len(board)
        n = len(board[0])
        
        unionFind = UnionFind(m * n + 1)
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'X':
                    continue
                
                for x in xrange(4):
                    new_i = i + offsets[x][0]
                    new_j = j + offsets[x][1]
                    
                    if new_i < 0 or new_i == m or new_j < 0 or new_j == n:  # bound node
                        unionFind.union(unionFind.find(i * n + j), unionFind.find(m * n))
                    
                    elif board[new_i][new_j] == 'O':
                        unionFind.union(unionFind.find(i * n + j), unionFind.find(new_i * n + new_j))
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'X':
                    continue
                
                if unionFind.find(i * n + j) != unionFind.find(m * n):
                    board[i][j] = 'X'
        
        
        
    
    
    def sol_TLE(self, board):
        if board is None or not board:
            return
        
        m = len(board)
        n = len(board[0])
        
        # polluted the 'O' without surrounded by 'X' with 'P'
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        '''
        A method to pollute the 'O' to 'P'
        '''
        def pollute(i, j):
            board[i][j] = 'P' # pollute
            for offset_i, offset_j in offsets:
                new_i = i + offset_i
                new_j = j + offset_j
                
                if new_i >= 0 and new_i < m and \
                    new_j >= 0 and new_j < n and \
                        board[new_i][new_j] == 'O':
                            pollute(new_i, new_j)
                            
        
        for i in xrange(n):
            if board[0][i] == 'O':
                pollute(0, i)
        
            if board[m - 1][i] == 'O':
                pollute(m - 1, i)
        
        for i in xrange(1, m - 1):
            if board[i][0] == 'O':
                pollute(i, 0)
            
            if board[i][n - 1] == 'O':
                pollute(i, n - 1)
                
        # set all the inner 'O' to 'X'
        for i in xrange(1, m):
            for j in xrange(1, n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        # purify the pollution
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'P':
                    board[i][j] = 'O'