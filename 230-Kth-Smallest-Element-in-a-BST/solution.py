# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        if root is None:
            return None
        
        ans = self.dfs(root, k)
        return ans[1]
        
    '''
    A method to traverse the whole tree
    @return the number of node in that subtree
    '''
    def dfs(self, root, k):
        if root is None:
            return 0, None
        
        left_count, ans = self.dfs(root.left, k)
        
        if ans is not None: # find the target value
            return left_count, ans
    
        if k == left_count + 1: # the root is the target value
            return left_count + 1, root.val
        
        right_count, ans = self.dfs(root.right, k - left_count - 1)
        
        return left_count + right_count + 1, ans
        
        
        