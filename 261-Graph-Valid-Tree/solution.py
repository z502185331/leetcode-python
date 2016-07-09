class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        graphs = {}
        marks = [0] * n
        
        # init the graph
        for i in xrange(n):
            graphs[i] = []
        
        for edge in edges:
            graphs[edge[0]].append(edge[1])
            graphs[edge[1]].append(edge[0])
            
        
        # traverse the whole graph
        if not self.dfs(0, graphs, marks, None):
            return False
        
        # check all the nodes has been traversed
        return 0 not in marks
    
    def dfs(self, cur, graphs, marks, prev):
        """
        A method to check whether there are any cycle
        """
        if marks[cur] == 1:
            return False
        
        marks[cur] = 1
        for neighbor in graphs[cur]:
            if marks[neighbor] == 2 or neighbor == prev:
                continue
            
            if not self.dfs(neighbor, graphs, marks, cur):
                return False
        
        marks[cur] = 2
        return True
        