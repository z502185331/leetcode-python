# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root is None:
            return None
        
        left_flag = self.find(root.left, p, q)
        right_flag = self.find(root.right, p, q)
        
        if root in [p, q]:
            if left_flag or right_flag:
                return root
        else:
            if left_flag and right_flag:
                return root
            elif left_flag:
                return self.lowestCommonAncestor(root.left, p, q)
            elif right_flag:
                return self.lowestCommonAncestor(root.right, p, q)
        
        
        
    
    '''
    A method to check whether the node is in the tree
    '''
    def find(self, root, p, q):
        if root is None:
            return False
            
        if root is p or root is q:
            return True
        
        return self.find(root.left, p, q) or self.find(root.right, p, q)