class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        # init the graph
        graph = {}
        for i in xrange(numCourses):
            graph[i] = []
    
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        
        # contains sorted nodes
        return self.topologicalSort(graph) if not self.hasCycle(graph) else []
    
    
    def hasCycle(self, graph):
        
        marks = [0] * len(graph)
        
        def dfs(cur):
            if marks[cur] == 1:
                return False

            marks[cur] = 1
            
            for i in graph[cur]:
                
                if not dfs(i):
                    return False
            
            marks[cur] = 2
            return True
            
        for i in xrange(len(graph)):
            if marks[i] == 2:
                continue
            
            if not dfs(i):
                return True
        
        return False
        
        
        
    def topologicalSort(self, graph):
        queue = []
        marks = [False] * len(graph)
        
        def dfs(cur):
            
            marks[cur] = True
            for next_course in graph[cur]:
                if not marks[next_course]:
                    dfs(next_course)
                    
            queue.insert(0, cur)
            
        
        for course in graph:
            if not marks[course]:
                dfs(course)
        
        return queue
        
        