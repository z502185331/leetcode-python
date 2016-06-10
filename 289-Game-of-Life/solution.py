class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or not board or not board[0]:
            return
        
        m = len(board)
        n = len(board[0])
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        
        for i in xrange(m):
            for j in xrange(n):
                count = 0
                for o in offsets:
                    new_i = i + o[0]
                    new_j = j + o[1]
                    if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and (board[new_i][new_j] & 1):
                        count += 1
                
                # the rightmost bit shows current state, the second bit shows next state
                if count == 2:
                    board[i][j] += board[i][j] << 1
                elif count == 3:
                    board[i][j] += 1 << 1
        
        # change to next state
        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1
                
        