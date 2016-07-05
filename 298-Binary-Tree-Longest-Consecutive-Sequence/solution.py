# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        
        return self.dfs(root, 0)
        
        
    def dfs(self, node, length):
        
        length += 1
        left_len, right_len = 0, 0
        if node.left is not None:
            if node.left.val == node.val + 1:
                left_len = self.dfs(node.left, length)
            else:
                left_len = self.dfs(node.left, 0)
        
        if node.right is not None:
            if node.right.val == node.val + 1:
                right_len = self.dfs(node.right, length)
            else:
                right_len = self.dfs(node.right, 0)
        
        return max(length, left_len, right_len)
        