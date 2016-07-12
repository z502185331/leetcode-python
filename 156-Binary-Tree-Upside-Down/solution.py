# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root is None or (root.left is None and root.right is None):
            return root
        
        left_node = self.upsideDownBinaryTree(root.left)
        
        root.left.left = root.right
        root.left.right = root
        
        root.left = None
        root.right = None
        
        return left_node
                
            