# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        res = []
        level = [] # a list of value in a level
        stack_odd = [root]  # a stack for odd level
        stack_even = [] # a stack for even level
        
        while stack_odd or stack_even:
            if stack_odd:
                while stack_odd:
                    node = stack_odd.pop()
                    level.append(node.val)
                    
                    if node.left is not None:
                        stack_even.append(node.left)
                    if node.right is not None:
                        stack_even.append(node.right)
                res.append(list(level))
                level = []
            else:
                while stack_even:
                    node = stack_even.pop()
                    level.append(node.val)
                    
                    if node.right is not None:
                        stack_odd.append(node.right)
                    if node.left is not None:
                        stack_odd.append(node.left)
                        
                res.append(list(level))
                level = []
        return res