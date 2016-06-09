class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if tickets is None or not tickets:
            return []
        
        d = {} # a dict store the <from> to <a list of to>
        for t in tickets:
            if t[0] not in d:
                d[t[0]] = [t[1]]
            else:
                d[t[0]].append(t[1])
        
        for l in d.values():
            l.sort()
    
        '''
        A method to find path by dfs, the depth should be less or equal than len(tickets)
        '''
        def dfs(depth, start, path):
            path.append(start)
            if depth == len(tickets):
                return True
            
            if start not in d or not d[start]:
                return False
            
            for i in xrange(len(d[start])):
                dest = d[start][i]
                d[start].remove(dest)
                if dfs(depth + 1, dest, path):
                    return True
                path.pop()
                d[start].insert(i, dest)
            return False
        
        path = []
        dfs(0, 'JFK', path)
        return path
            