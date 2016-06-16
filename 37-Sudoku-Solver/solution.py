class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        row_sets = []
        col_sets = []
        squ_sets = []
        
        # init lists of sets
        for i in xrange(9):
            row_sets.append(set())
            col_sets.append(set())
            squ_sets.append(set())
        
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] != '.':
                    row_sets[i].add(board[i][j])
                    col_sets[j].add(board[i][j])
                    squ_sets[(i / 3) * 3 + (j / 3) % 3].add(board[i][j])
        
        '''
        A method to fill number by dfs
        '''
        def solver(i, j):
            if i == 9:
                return True
            
            # get the next (i, j)
            next_i, next_j = i, j
            if j + 1 == 9:
                next_j = 0
                next_i += 1
            else:
                next_j += 1
                
                
            if board[i][j] != '.':
                return solver(next_i, next_j)
            
            for num in xrange(1, 10):
                str_num = str(num)
                if str_num in row_sets[i] or \
                    str_num in col_sets[j] or \
                        str_num in squ_sets[(i / 3) * 3 + (j / 3) % 3]:
                    
                    continue
                
                board[i][j] = str_num
                row_sets[i].add(board[i][j])
                col_sets[j].add(board[i][j])
                squ_sets[(i / 3) * 3 + (j / 3) % 3].add(board[i][j])
                
                if solver(next_i, next_j):
                    return True
                
                row_sets[i].remove(board[i][j])
                col_sets[j].remove(board[i][j])
                squ_sets[(i / 3) * 3 + (j / 3) % 3].remove(board[i][j])
            
            board[i][j] = '.'
            return False
            
        solver(0, 0)
        
                
                
            