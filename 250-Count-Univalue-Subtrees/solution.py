# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        return self.traverse(root, None)[0]
    
    def traverse(self, root, prev):
        """
        return: the number of uni-tree, the value of uni-tree
        rtype: int, int
        """
        if root is None:
            return 0, prev
        
        if root.left is None and root.right is None:
            return 1, root.val
            
        left_count, left_val = self.traverse(root.left, root.val)
        right_count, right_val = self.traverse(root.right, root.val)
        
        if root.val == left_val and root.val == right_val:
            return left_count + right_count + 1, root.val
        else:
            return left_count + right_count, None
        
        