# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        res = []
        
        def dfs(root, path, cur):
            if root is None:
                return
            
            cur += root.val
            path.append(root.val)
            
            # leaf node
            if root.left is None and root.right is None:
                if cur == sum:
                    res.append(list(path))
                path.pop()
                return
            
            dfs(root.left, path, cur)
            dfs(root.right, path, cur)
            path.pop()
            
        dfs(root, [], 0)
        return res
            