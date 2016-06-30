# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        
        if root is None:
            return 
        
        queue = [root]
        
        while queue:
            size = len(queue)
            
            for i in xrange(size):
                node = queue.pop(0)
                
                # the rightmost node
                if i != size - 1 and queue:
                    node.next = queue[0]
                
                if node.left is not None:
                    queue.append(node.left)
                
                if node.right is not None:
                    queue.append(node.right)