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
    
        return self.traverse(root)[0]
    
    def traverse(self, root):
        if root is None:
            return True, sys.maxint, -sys.maxint - 1
            
        left_flag, left_lower, left_upper = self.traverse(root.left)
        right_flag, right_lower, right_upper = self.traverse(root.right)
        
        if not left_flag or not right_flag or root.val <= left_upper or root.val >= right_lower:
            return False, 0, 0
        
        else:
            return True, min(left_lower, root.val), max(right_upper, root.val)
    
    
    def sol_stack(self, root):
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
                
                
                
                