# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        res = []
        level = []  # a list to store the val in a level
        queue = [root]
        
        while queue:
            size = len(queue)
            for i in xrange(size):
                node = queue.pop(0)
                level.append(node.val)
                
                # push the children of node to queue
                if node.left is not None:
                    queue.append(node.left)
                    
                if node.right is not None:
                    queue.append(node.right)
                
            # when traverse a level
            res.append(list(level))
            level = []
            
        return res