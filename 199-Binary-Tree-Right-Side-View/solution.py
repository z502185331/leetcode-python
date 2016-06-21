# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        self.dfs(root, 0, -1, res)
        return res
    
    '''
    A method to add value to res, if there is no right node.
    @return the depth of root
    '''
    def dfs(self, root, depth, r_depth, res):
        if root is None:
            return depth - 1
        
        if depth > r_depth:
            res.append(root.val)
        
        cur_r_depth = self.dfs(root.right, depth + 1, r_depth, res)
        cur_l_depth = self.dfs(root.left, depth + 1, max(r_depth, cur_r_depth), res)
        
        return max(cur_r_depth, cur_l_depth)