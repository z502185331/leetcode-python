class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        if not numCourses or not prerequisites:
            return True
        
        # save the prerequistes into a graph
        graph = {}
        for i in xrange(numCourses):
            graph[i] = []
            
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
        
        marks = [0] * numCourses
        
        def dfs(cur):
            marks[cur] = -1
            for i in graph[cur]:
                if marks[i] == -1:
                    return False
                    
                if not dfs(i):
                    return False
            
            marks[cur] = 1
            return True
            
        
        for i in xrange(numCourses):
            if marks[i] != 1:
                if not dfs(i):
                    return False
        
        return True
            
            
        