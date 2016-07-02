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
        
        # return self.sol_iter(root)
        return self.sol_rec1(root.left, root.right)
        
    def sol_iter(self, root):
        stack_left = [root]
        stack_right = [root]
        
        left, right = root.left, root.right
        while stack_left and stack_right:
            if left is not None and right is not None:
                if left.val != right.val:
                    return False
                stack_left.append(left)
                stack_right.append(right)
                left = left.left
                right = right.right
            elif left is None and right is None:
                left = stack_left.pop()
                right = stack_right.pop()
                left = left.right
                right = right.left
            else:
                return False
        return True
        
        
    
    
    def sol_rec(self, root):
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
    
    def sol_rec1(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            return root1.val == root2.val and \
                self.sol_rec1(root1.left, root2.right) and \
                    self.sol_rec1(root1.right, root2.left)
        else:
            return False
        
        
        