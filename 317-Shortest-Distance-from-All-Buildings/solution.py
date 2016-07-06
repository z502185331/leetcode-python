class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        distances = [[0] * n for _ in xrange(m)]
        reachCount = [[0] * n for _ in xrange(m)]
        self.offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # count the total number of hourse
        self.totalHouse = 0
        for i in xrange(m):
                for j in xrange(n):
                    if grid[i][j] == 1:
                        self.totalHouse += 1
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    if not self.bfs(grid, distances, reachCount, i, j):
                        return -1
        
        minDis = sys.maxint
        for i in xrange(m):
            for j in xrange(n):
                if reachCount[i][j] != self.totalHouse:    #ignore building and obstacle
                    continue
                minDis = min(minDis, distances[i][j])
        return minDis
    
    
    def bfs(self, grid, distances, reachCount, x, y):
        m, n = len(grid), len(grid[0])
        marks = [[False] * n for _ in xrange(m)]   # a set contains all the visited places
        queue = [(x, y)]
        count = 0
        distance = 0
        while queue:
            size = len(queue)
            distance += 1
            for _ in xrange(size):
                cur_x, cur_y = queue.pop(0)
                
                for offset in self.offsets:
                    next_x = cur_x + offset[0]
                    next_y = cur_y + offset[1]

                    if 0 <= next_x < m and 0 <= next_y < n and not marks[next_x][next_y]:
                        if grid[next_x][next_y] == 0:
                            distances[next_x][next_y] += distance
                            marks[next_x][next_y] = True
                            reachCount[next_x][next_y] += 1
                            queue.append((next_x, next_y))
                        elif grid[next_x][next_y] == 1:
                            count += 1
                            marks[next_x][next_y] = True
        
        return count == self.totalHouse
                         
                
                
        