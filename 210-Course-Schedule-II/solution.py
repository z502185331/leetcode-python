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
        return self.topologicalSort(graph)
        
        
        
    def topologicalSort(self, graph):
        queue = []
        marks = [0] * len(graph)
        
        def dfs(cur):
            if marks[cur] == 1:
                return False
            
            marks[cur] = 1
            for next_course in graph[cur]:
                if marks[next_course] == 2:
                    continue
                
                if not dfs(next_course):
                    return False
                    
            queue.insert(0, cur)
            marks[cur] = 2
            return True
            
        
        for course in graph:
            if marks[course] == 2:
                continue
            
            if not dfs(course):
                return []
        
        return queue
        
        