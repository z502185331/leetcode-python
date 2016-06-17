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
        
        marks = [False] * numCourses
        s = set()
        
        def dfs(cur):
            if marks[cur]:
                return False
            
            
            marks[cur] = True
            
            for i in graph[cur]:
                
                if not dfs(i):
                    return False
            
            s.add(cur)
            marks[cur] = False
            return True
            
        
        for i in xrange(numCourses):
            if i in s:
                continue
            
            if not dfs(i):
                return False
        
        return True
            
            
        