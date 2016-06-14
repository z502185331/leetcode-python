# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
        
        self.queue = []
        self.pushToQueue(root.left)
        return self.checkSymm(root.right)
        
        
    
    '''
    A method to push node into a queue
    '''
    def pushToQueue(self, root):
        self.queue.append(root)
        if root is None:
            return
        
        self.pushToQueue(root.left)
        self.pushToQueue(root.right)
    
    '''
    A method to check the right child is symmetric to left child
    :rtype: bool
    '''
    def checkSymm(self, root):
        node = self.queue.pop(0)
        
        if root is None and node is None:
            return True
        elif root is not None and node is not None:
            if root.val != node.val:
                return False
            return self.checkSymm(root.right) and self.checkSymm(root.left)
        else:
            return False
        
        
        