class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        if n == 1:
            return [0]
        
        count = [0] * n # a list record the number of edge connected with node i
        
        # construct a dict <node> - <neighbors>
        graph = {}
        for e in edges:
            graph[e[0]] = graph.get(e[0], []) + [e[1]]
            graph[e[1]] = graph.get(e[1], []) + [e[0]]
            count[e[0]] += 1
            count[e[1]] += 1
        
        queue = []
        
        # push the node with count 1 into the queue, which is leaf node
        for i, c in enumerate(count):
            if c == 1:
                queue.append(i)
        
        # when the length of queue less than 2, the rest are the root with MHT
        while n > 2:
            size = len(queue)
            for i in xrange(size):
                n -= 1
                node = queue.pop(0)
                
                for neighbor in graph[node]:
                    count[neighbor] -= 1
                    if count[neighbor] == 1:
                        queue.append(neighbor)
        return queue
            
        
            