# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        
        res = []
        
        def dfs(node, path):
            if node is None:
                return 
            
            if path:    # start of path
                path += '->' + str(node.val)
            else:
                path += str(node.val)
            
            if node.left is None and node.right is None:
                res.append(path)
                return
            
            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, '')
        return res
            