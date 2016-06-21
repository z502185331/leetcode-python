# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
        
        stack = []
        res = []
        
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
                
            else:
                if not stack:
                    break
                
                root = stack.pop()
                res.append(root.val)
                root = root.right
        
        return res