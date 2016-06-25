# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
        
        preNode = None
        stack = []
        
        # inorder traverse the tree
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            
            else:
                if not stack:
                    break
                root = stack.pop()
                
                if preNode is not None and preNode.val >= root.val:
                    return False
                
                preNode = root
                root = root.right
        
        return True
                
                
                
                