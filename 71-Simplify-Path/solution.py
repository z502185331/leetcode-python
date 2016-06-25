class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        if not path:
            return path
        
        stack = []
        
        i = 0
        m = len(path)
        
        while i < m:
            if path[i] == '/':
                i += 1
                continue
            
            cur = ''
            while i < m and path[i] != '/':
                cur += path[i]
                i += 1
            
            if cur == '.':
                continue
            
            elif cur == '..':
                if stack:
                    stack.pop()
            
            else:
                stack.append(cur)
        
        return '/' + '/'.join(stack)