class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        
        if not preorder:
            return False
        
        stack = []
        
        # '#' serve as a terminator
        # A node can be popped out if there are two terminator after it, 
        # and become a terminator
        
        
        l = preorder.split(',')
        
        if ((len(l) & 1) == 0): # the len of preorder cannot be even
            return False
        
        if l[0] == '#':
            return len(l) == 1
        
        stack.append([l[0], 0])
        for i in xrange(1, len(l)):    # stack always has elem except the last node is processed
            if l[i] == '#':
                stack[-1][1] += 1
            else:
                stack.append([l[i], 0]) # the second elem is the count of terminator after it
            
            # if the count is 2, pop out the top of stack and add the count to the newly top node
            while stack and stack[-1][1] == 2:
                stack.pop()
                if stack:
                    stack[-1][1] += 1
                else:
                    if i != len(l) - 1:
                        return False
        
        return stack == []
                    
        