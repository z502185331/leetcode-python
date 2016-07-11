# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        res = []
        while root is not None:
            leaves = []
            root = self.traverse(root, leaves)
            res.append(leaves)
        return res
    
    
    def traverse(self, root, leaves):
        """
        :type root: TreeNode
        :type leaves: List[int]
        """
        if root is None:
            return None
        
        if root.left is None and root.right is None:     # leaf node
            leaves.append(root.val)
            return None
        
        root.left = self.traverse(root.left, leaves)
        root.right = self.traverse(root.right, leaves)
        return root