class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        parents = [x for x in xrange(m * n)]
        
        self.count = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    self.count += 1
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '0':
                    continue
                
                offset = i * n + j
                # find the four direction
                if i - 1 >= 0 and grid[i - 1][j] == '1':
                    self.union(parents, offset, offset - n)
                
                if j + 1 < n and grid[i][j + 1] == '1':
                    self.union(parents, offset, offset + 1)
                    
                if i + 1 < m and grid[i + 1][j] == '1':
                    self.union(parents, offset, offset + n)
                    
                if j - 1 >= 0 and grid[i][j - 1] == '1':
                    self.union(parents, offset, offset - 1)
                    
        return self.count
    
    '''
    A method to union the o1, and o2
    '''
    def union(self, parents, o1, o2):
        root1 = self.root(parents, o1)
        root2 = self.root(parents, o2)
        
        if root1 == root2:  # when two islands are already connected
            return
        
        parents[root1] = root2
        self.count -= 1
    
    
    '''
    A method to find the root of parent
    '''
    def root(self, parents, i):
        while parents[i] != i:
            parents[i] = parents[parents[i]]
            i = parents[i]
        
        return i
                    