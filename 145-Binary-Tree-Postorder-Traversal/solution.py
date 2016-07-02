# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        stack = []
        res = []
        
        while stack or root is not None:
            if root is not None:
                if root.right is not None:
                    stack.append(root.right)
                
                stack.append(root)
                root = root.left;
            
            else:
                
                root = stack.pop()
                
                # deal with right child first
                if stack and stack[-1] is root.right:
                    tmp = stack.pop()
                    stack.append(root)
                    root = tmp
                
                else:
                    res.append(root.val)
                    root = None
        
        return res
                    
                    