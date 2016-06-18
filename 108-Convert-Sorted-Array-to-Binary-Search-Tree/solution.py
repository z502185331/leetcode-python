# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        return self.build(nums, 0, len(nums) - 1)
        
    
    def build(self, nums, start, end):
        if start > end:
            return None
        
        mid = start + (end - start) / 2
        node = TreeNode(nums[mid])
        left_node = self.build(nums, start, mid - 1)
        right_node = self.build(nums, mid + 1, end)
        
        node.left = left_node
        node.right = right_node
        
        return node