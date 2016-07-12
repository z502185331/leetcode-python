# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        while root is not None and root.val <= p.val:
            root = root.right
        
        if root is None:
            return None
        
        left_node = self.inorderSuccessor(root.left, p)
        return left_node if (left_node is not None and left_node.val > p.val) else root
        
    def sol_recursion(self, root, p):
        if root is None:
            return None
            
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left_node = self.inorderSuccessor(root.left, p)
            return left_node if left_node is not None else root
        
        
        
        