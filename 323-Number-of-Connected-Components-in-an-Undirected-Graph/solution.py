class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        graphs = {}
        for i in xrange(n):
            graphs[i] = []
        
        for edge in edges:
            graphs[edge[0]].append(edge[1])
            graphs[edge[1]].append(edge[0])
        
        marks = [False] * n
        count = 0
        
        for i in xrange(n):
            if marks[i]:
                continue
            
            count += 1  # a new component
            self.dfs(i, graphs, marks)
        
        return count
    
    
    def dfs(self, cur, graphs, marks):
        if marks[cur]:
            return
        
        marks[cur] = True
        for neighbor in graphs[cur]:
            if marks[neighbor]:
                continue
            
            self.dfs(neighbor, graphs, marks)
        
        
            