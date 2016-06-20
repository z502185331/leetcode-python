# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
        
        stack = [root]
        res = [root.val]
        root = root.left
        
        while True:
            if root is not None:
                stack.append(root)
                res.append(root.val)
                root = root.left
            
            else:
                if not stack:   # if no node in stack, traverse finished
                    break
                
                root = stack.pop()
                root = root.right
                
        return res
                
                
            
        