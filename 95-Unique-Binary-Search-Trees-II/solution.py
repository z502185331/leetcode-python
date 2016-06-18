# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        
        return self.build(1, n)
    
    def build(self, start, end):
        if start > end:
            return [None]
        
        res = []
        for i in xrange(start, end + 1):
            left_list = self.build(start, i - 1)
            right_list = self.build(i + 1, end)

            for left_node in left_list:
                for right_node in right_list:
                    node = TreeNode(i)
                    node.left = left_node
                    node.right = right_node
                    res.append(node)
        
        return res
                    